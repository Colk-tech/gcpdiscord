from typing import Optional

import discord

from src.utils.singleton import Singleton
from src.discord.message_handler import MessageHandler
from src.message.create_root import message
from config import (
    DISCORD_INTENTS,
    DISCORD_TOKEN,
    DISCORD_MAIN_CHANNEL_ID)


class DiscordBOT(Singleton, discord.Client):
    def __init__(self):
        super(DiscordBOT, self).__init__(
            presences=True,
            guild_subscriptions=True,
            intents=DISCORD_INTENTS)
        self.guild: Optional[discord.Guild] = None

    def launch(self):
        self.run(DISCORD_TOKEN)

    async def on_ready(self):
        await self.send_to_id_channel(DISCORD_MAIN_CHANNEL_ID, content=message.get("LOGIN"))

        if len(self.guilds) > 1:
            raise RuntimeError("This bot supports only one server to be alive.")

        self.guild = self.guilds[0]

    async def on_message(self, message: discord.Message):
        handler = MessageHandler(message)
        await handler.execute()

    async def send_to_id_channel(self, channel_id: int, **kwargs):
        channel = self.get_channel(channel_id)
        await channel.send(**kwargs)
