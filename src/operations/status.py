from typing import List

import discord
from googleapiclient.discovery import build

from src.operations.operation_abs import OperationOrigin
from src.utils.unauthorized import send_unauthorized_message
from src.gcp.create_gcp_holder import gcp
from src.message.create_root import message
from config import COMMAND_PREFIX


class Status(OperationOrigin):
    MY_INDEX: str = "status"
    IS_AUTHORIZATION_NEEDED: bool = False

    def __init__(self):
        super(Status, self).__init__()
        self.MY_INDEX: str = "status"
        self.IS_AUTHORIZATION_NEEDED: bool = True

    async def execute(self, raw_message: discord.Message):
        if not self.check_permitted(member=raw_message.author):
            await send_unauthorized_message(channel=raw_message.channel)
            return

        await raw_message.channel.send(message.get("CHECK_STATUS", gcp_status=gcp.get_instance()["status"]))
