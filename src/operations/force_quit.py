import time
from typing import List

import discord
from googleapiclient.discovery import build

from src.operations.operation_abs import OperationOrigin
from src.utils.unauthorized import send_unauthorized_message
from src.gcp.create_gcp_holder import gcp
from src.message.create_root import message


class ForceQuit(OperationOrigin):
    MY_INDEX: str = "forcequit"
    IS_AUTHORIZATION_NEEDED: bool = False

    def __init__(self):
        super(ForceQuit, self).__init__()
        self.MY_INDEX: str = "forcequit"
        self.IS_AUTHORIZATION_NEEDED: bool = True

    async def execute(self, raw_message: discord.Message):
        if not self.check_permitted(member=raw_message.author):
            await send_unauthorized_message(channel=raw_message.channel)
            return

        if not (len(raw_message.content.split()) >= 3):
            await raw_message.channel.send(message.get("NEED_CONFIRM_TO_FORCE_QUIT"))
            return

        if not raw_message.content.split()[2].lower().startswith("--confirm"):
            await raw_message.channel.send(message.get("BEGIN_FORCE_QUIT_OPERATION"))
            return

        await raw_message.channel.send(message.get("REQUEST_RECEIVED",
                                                   member_name=raw_message.author.display_name,
                                                   guild_name=raw_message.guild.name))

        gcp_status = gcp.get_instance()["status"]

        await raw_message.channel.send(message.get("CHECK_STATUS", gcp_status=gcp_status))

        ERROR_MESSAGE = "Though we waited for 3 minutes to stop the GCP instance, it has not started yet."

        if gcp_status == "TERMINATED":
            await raw_message.channel.send(message.get("ALREADY_IN_THE_STATUS", gcp_status=gcp_status))
            return

        await raw_message.channel.send(message.get("BEGIN_FORCE_QUIT_OPERATION"))

        gcp.RESOURCE.instances().stop(**gcp.INSTANCE_INFO).execute()

        challenging_times = 0

        while True:
            challenging_times += 1
            instance: dict = gcp.RESOURCE.instances().get(**gcp.INSTANCE_INFO).execute()

            if instance["status"] == "TERMINATED":
                await raw_message.channel.send(message.get("OPERATION_COMPLETED", operation_name=self.MY_INDEX))
                return
            if challenging_times >= 60:
                await raw_message.channel.send(message.get("ERROR_OCCURED", stack_trace=ERROR_MESSAGE))
                return

            time.sleep(3)
