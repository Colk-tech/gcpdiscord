import abc
from typing import Optional

import discord

from config import PERMITTED_ROLE_IDS
from src.utils.unauthorized import send_unauthorized_message


class OperationOrigin(metaclass=abc.ABCMeta):
    MY_INDEX: str = ""
    IS_AUTHORIZATION_NEEDED: bool = True

    def __init__(self):
        self.MY_INDEX: str = ""
        self.IS_AUTHORIZATION_NEEDED: bool = True
        self.__raw_message: Optional[discord.Message] = None

    @abc.abstractmethod
    async def execute(self, raw_message: discord.Message):
        self.__raw_message = raw_message

        if not self.check_permitted(raw_message.author):
            await send_unauthorized_message(channel_id=raw_message.channel.id)
            return

    @abc.abstractmethod
    def check_permitted(self, member: discord.Member) -> bool:
        permitted_role_ids = PERMITTED_ROLE_IDS
        member_role_ids = list(map((lambda role: role.id), member.roles))

        if not self.IS_AUTHORIZATION_NEEDED:
            return True

        if len(set(member_role_ids) & set(permitted_role_ids)) <= 0:
            return False
        else:
            return True
