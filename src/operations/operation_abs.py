import abc
from typing import Optional, List

import discord

from config import PERMITTED_ROLE_IDS


class OperationOrigin(metaclass=abc.ABCMeta):
    MY_INDEX: str = ""
    IS_AUTHORIZATION_NEEDED: bool = True

    def __init__(self):
        self.MY_INDEX: str = ""
        self.IS_AUTHORIZATION_NEEDED: bool = True
        self.__raw_message: Optional[discord.Message] = None
        self.__channel: Optional[discord.TextChannel] = None
        self.__message_author: Optional[discord.Member] = None
        self.__split_message: Optional[List[str]] = None

    def check_permitted(self, member: discord.Member) -> bool:
        permitted_role_ids = PERMITTED_ROLE_IDS
        member_role_ids = list(map((lambda role: role.id), member.roles))

        if not self.IS_AUTHORIZATION_NEEDED:
            return True

        if len(set(member_role_ids) & set(permitted_role_ids)) <= 0:
            return False

        else:
            return True
