import asyncio

from typing import List, Optional

import discord

from src.gcp_command_manager import GCPCommandRequest
from src.config import (
    DISCORD_INTENTS,
    DISCORD_TOKEN,
    PERMITTED_ROLE_IDS,
    DISCORD_MAIN_CHANNEL_ID,
    COMMAND_PREFIX,
    DISCORD_MINECRAFT_CONSOLE_CHANNEL_ID
    )
from src.messages import *

SHUTDOWN_WAIT_TIME: int = 300


class MainClient(discord.Client):
    def __init__(self):
        super(MainClient, self).__init__(presences=True, guild_subscriptions=True, intents=DISCORD_INTENTS)
        self.main_channel: Optional[discord.TextChannel] = None
        self.console_channel: Optional[discord.TextChannel] = None

    @staticmethod
    def is_authorized_member(member: discord.Member, permitted_role_ids: List[int]) -> bool:
        member_role_ids = list(map((lambda role: role.id), member.roles))
        if len(set(member_role_ids) & set(permitted_role_ids)) <= 0:
            return False
        else:
            return True

    def launch(self):
        self.run(DISCORD_TOKEN)

    async def on_ready(self):
        self.main_channel = self.get_channel(DISCORD_MAIN_CHANNEL_ID)
        self.console_channel = self.get_channel(DISCORD_MINECRAFT_CONSOLE_CHANNEL_ID)

    async def on_message(self, message: discord.Message):
        content = message.content
        author = message.author
        channel = message.channel

        if not content.lower().startswith(COMMAND_PREFIX):
            return

        if not self.is_authorized_member(author, PERMITTED_ROLE_IDS):
            await channel.send(PERMISSION_DENIED_MESSAGE)

        if not message.content.split()[1].lower() in ["start", "stop"]:
            return

        operation = message.content.split()[1].lower()

        await channel.send(REQUEST_RECEIVED)
        message_content = START_REQUEST_RECEIVED_MESSAGE if operation == "start" else STOP_REQUEST_RECEIVED_MESSAGE
        await channel.send(message_content)

        if operation == "stop":
            await self.pre_stop_operation(channel=channel)

        try:
            command = GCPCommandRequest(operation=operation)

            if command.check_already_in_status_of(operation=operation):
                await channel.send(INSTANCE_IS_ALREADY_IN_REQUESTED_STATUS.format(operation))
                return

            command.execute()

            await channel.send(OPERATION_COMPLETED_MESSAGE.format(operation))

        except Exception as e:
            await channel.send(ERROR_OCCURRED_MESSAGE.format(e))
            raise e

    async def pre_stop_operation(self, channel: discord.TextChannel):
        await channel.send(PRE_STOP_OPERATION_PROCESSING)
        await self.console_channel.send("stop")
        await asyncio.sleep(SHUTDOWN_WAIT_TIME)
