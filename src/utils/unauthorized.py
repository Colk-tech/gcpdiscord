from src.discord.create_bot import bot

from src.message.create_root import message


async def send_unauthorized_message(channel_id: int) -> None:
    await bot.send_to_id_channel(channel_id=channel_id,
                                 content=message.get("PERMISSION_DENIED"))
