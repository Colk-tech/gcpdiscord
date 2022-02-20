import discord

from src.message.create_root import message


async def send_unauthorized_message(channel: discord.TextChannel) -> None:
    await channel.send(content=message.get("PERMISSION_DENIED"))
