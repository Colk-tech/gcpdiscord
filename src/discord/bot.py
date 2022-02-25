from typing import Optional

import discord

from src.util.singleton import Singleton

from src.discord.embed.factory.exception import ExceptionEmbedFactory
from src.discord.handler.rooter import MessageHandler

from config import (
    DISCORD_INTENTS,
    DISCORD_TOKEN,
    DISCORD_MAIN_CHANNEL_ID
)


class DiscordBOT(Singleton, discord.Client):
    def __init__(self):
        super(DiscordBOT, self).__init__(
            presences=True,
            guild_subscriptions=True,
            intents=DISCORD_INTENTS)
        self.guild: Optional[discord.Guild] = None
        self.main_channel: Optional[discord.TextChannel] = None

    def launch(self):
        self.run(DISCORD_TOKEN)

    async def on_ready(self):
        self.main_channel = self.get_channel(DISCORD_MAIN_CHANNEL_ID)

        if self.main_channel is None:
            raise RuntimeError(
                f"The channel whose id is '{DISCORD_MAIN_CHANNEL_ID}' was not found."
                f"Make sure the '{DISCORD_MAIN_CHANNEL_ID}' really exists."
            )
            exit()

        if len(self.guilds) > 1:
            err: RuntimeError = RuntimeError(
                "Though this bot can be active in ONLY ONE server, "
                f"this bot is on multiple ({len(self.guilds)}) servers. "
                "Kick from any other servers than you want to use."
            )

            embed: discord.Embed = ExceptionEmbedFactory(
                exception=err
            ).make()

            await self.main_channel.send(embed=embed)

            raise err
            exit()

        self.guild = self.guilds[0]

    async def on_message(self, message):
        handler: MessageHandler = MessageHandler(
            message=message,
            context={
                "guild": self.guild,
                "main_channel": self.main_channel
            })

        try:
            await handler.execute()
        except Exception as e:
            embed: discord.Embed = ExceptionEmbedFactory(
                exception=e
            ).make()
            await self.main_channel.send(embed=embed)

            raise e
