from typing import List, Dict

from discord.message import Message

from config import COMMAND_PREFIX

from src.discord.handler.operations import OPERATIONS


class MessageHandler:
    def __init__(self, message: Message, context: Dict):
        self.__message: Message = message
        self.__divided: List[str] = message.content.split()
        self.__context: Dict = context
        # Real Signature: List[class extends src.discord.operations.abs.AbstractOperation]
        self.__task_schedules: List[type] = []

        self.__context["divided"] = self.__divided

    def __is_command(self) -> bool:
        if len(self.__divided) <= 0:
            return False

        if self.__divided[0].lower() == COMMAND_PREFIX:
            return True

        return False

    def __root(self):
        command: str = self.__divided[1].lower()

        for operation in OPERATIONS:
            if command == operation.MY_INDEX:
                self.__task_schedules.append(operation)

    async def __execute(self):
        for task_schedule in self.__task_schedules:
            task = task_schedule(
                message=self.__message,
                context=self.__context,
            )
            await task.execute()

    async def execute(self):
        if not self.__is_command():
            return

        self.__root()

        await self.__execute()
