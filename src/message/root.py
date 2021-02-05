from typing import Dict
import yaml
import re

from src.utils.singleton import Singleton
from config import MESSAGE_FILE_PATH


class MessageRoot(Singleton):
    def __init__(self) -> None:
        self.__messages: dict = self.__get_message_dict()

    @staticmethod
    def __get_message_dict() -> dict:
        with open(MESSAGE_FILE_PATH, "r") as stream:
            data: dict = yaml.safe_load(stream)
        return data

    def get(self, key: str, **kwargs: Dict) -> str:
        arguments: Dict = kwargs
        composing: str = self.__messages[key]

        for key, value in arguments.items():
            if value is None or value == "":
                arguments.pop(key)

        try:
            composing = composing.format(**kwargs)
        except KeyError as e:
            raise RuntimeError(f"Invalid key has passed while parsing message: {composing}.\n"
                               f"Make sure all the keys exists.")

        return composing
