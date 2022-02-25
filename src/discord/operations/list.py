from typing import Dict

from discord import Message, Embed

from src.gce.client import GCEClient

from src.discord.operations.abs import AbstractOperation
from src.discord.embed.factory.instance_list import InstanceListEmbedFactory


class StatusList(AbstractOperation):
    MY_INDEX: str = "list"
    IS_AUTHORIZATION_NEEDED: bool = False

    def __init__(self, message: Message, context: Dict):
        self.__message: Message = message
        self.__context: Dict = context

    def is_authorized(self) -> bool:
        return True

    async def execute(self):
        instances = GCEClient().get_instances()

        embed: Embed = InstanceListEmbedFactory(
            instances=instances
        ).make()

        await self.__message.channel.send(embed=embed)
