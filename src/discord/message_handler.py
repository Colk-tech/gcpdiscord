from typing import Optional

import discord

from config import COMMAND_PREFIX
from src.operations.rooter import get_operation
from src.message.create_root import message


class MessageHandler:
    def __init__(self, message: discord.Message) -> None:
        self.__raw_message: discord.Message = message
        self.__content: str = message.content
        self.__channel: discord.TextChannel = message.channel
        self.__split_message: str = message.content.split()
        self.__index: Optional[str] = None

    async def execute(self):
        if await self.__pre_rooting_process():
            await self.__rooting(self.__index)
        return

    async def __pre_rooting_process(self) -> bool:
        if self.__raw_message.author.bot:
            return False

        if not self.__content.lower().startswith(COMMAND_PREFIX):
            return False

        if not len(self.__split_message) >= 2:
            await self.__rooting("help")
            return False

        self.__index = self.__split_message[1].lower()
        return True

    async def __rooting(self, operation_name: str):
        # 入力されたコマンドに対してのOperation型を継承したクラスを受け取る
        operation: Optional[type] = get_operation(operation_name)

        # ヒットしない場合
        if operation is None:
            await self.__channel.send(content=message.get("NO_SUCH_COMMAND"))
            return

        await operation().execute(self.__raw_message, self.__split_message)
