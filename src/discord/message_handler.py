from typing import Optional

import discord

from config import COMMAND_PREFIX
from src.operations.rooter import get_operation
from src.discord.create_bot import bot
from src.message.create_root import message


class MessageHandler:
    def __init__(self, message: discord.Message) -> None:
        self.__raw_message: discord.Message = message
        self.__channel_id: int = message.channel.id
        self.__content: str = message.content
        self.__split_message: str = message.content.split()
        self.__index: Optional[str] = None

    async def execute(self):
        if not self.__pre_rooting_process():
            await self.__rooting(self.__index)
        return

    def __pre_rooting_process(self) -> bool:
        if not self.__content.lower().startswith(COMMAND_PREFIX):
            return False

        if not len(self.__split_message) >= 2:
            self.__rooting("help")
            return False

        self.__index = self.__split_message[1].lower()

    async def __rooting(self, operation_name: str):
        # 入力されたコマンドに対してのOperation型を継承したクラスを受け取る
        operation: Optional[type] = get_operation(operation_name)

        # ヒットしない場合
        if operation is None:
            await bot.send_to_id_channel(channel_id=self.__channel_id, content=message.get("NO_SUCH_COMMAND"))

        await operation().execute(self.__raw_message)
