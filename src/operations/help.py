from typing import List

import discord

from src.operations.operation_abs import OperationOrigin
from src.utils.unauthorized import send_unauthorized_message
from src.message.create_root import message
from config import COMMAND_PREFIX


class Help(OperationOrigin):
    MY_INDEX: str = "help"
    IS_AUTHORIZATION_NEEDED: bool = False

    def __init__(self):
        super(Help, self).__init__()
        self.MY_INDEX: str = "help"
        self.IS_AUTHORIZATION_NEEDED: bool = True

    async def execute(self, raw_message: discord.Message, split_message: List[str]):
        if not self.check_permitted(member=raw_message.author):
            await send_unauthorized_message(channel=raw_message.channel)
            return

        await raw_message.channel.send(message.get("HELP", prefix=COMMAND_PREFIX))
