import discord

from src.config import DISCORD_INTENTS, DISCORD_TOKEN, PERMITTED_ROLE_IDS
from src.config import PERMISSION_DENIED_MESSAGE, ERROR_OCCURRED_MESSAGE, COMMAND_PREFIX
from src.execute_gcp_command import GCPCommandRequest


class MainClient(discord.Client):
    def __init__(self):
        super(MainClient, self).__init__(presences=True, guild_subscriptions=True, intents=DISCORD_INTENTS)

    def launch(self):
        self.run(DISCORD_TOKEN)

    async def on_message(self, message: discord.Message):
        content = message.content
        author = message.author
        channel = message.channel

        author_role_ids = list(map((lambda role: role.id), author.roles))

        if not content.lower().startswith(COMMAND_PREFIX):
            return

        if len(set(PERMITTED_ROLE_IDS) & set(author_role_ids)) <= 0:
            await channel.send(PERMISSION_DENIED_MESSAGE)
            return

        if not message.content.split()[1].lower() in ["start", "stop"]:
            return

        else:
            operation = message.content.split()[1].lower()
            try:
                command = GCPCommandRequest(operation=operation)
                command.execute()
            except Exception as e:
                await channel.send(ERROR_OCCURRED_MESSAGE.format(e))

    async def on_ready(self):
        pass
