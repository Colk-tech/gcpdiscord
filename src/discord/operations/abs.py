from typing import Dict
from abc import ABCMeta, abstractmethod

from discord import Message


class AbstractOperation(metaclass=ABCMeta):
    MY_INDEX: str = ""
    IS_AUTHORIZATION_NEEDED: bool = False

    @abstractmethod
    def __init__(self, message: Message, context: Dict):
        self.__message: Message = message
        self.__context: Dict = context

    @abstractmethod
    def is_authorized(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def execute(self):
        raise NotImplementedError()
