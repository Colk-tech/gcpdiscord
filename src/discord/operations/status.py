from typing import Dict

from discord import Message, Embed

from src.gce.client import GCEClient
from src.gce.type.instance import GCEInstanceRepresentingWrapper
from src.gce.exception.gce import InstanceNotFound

from src.discord.operations.abs import AbstractOperation
from src.discord.embed.factory.not_found import InstanceNotFoundEmbedFactory
from src.discord.embed.factory.incorrect_command import IncorrectCommandEmbedFactory
from src.discord.embed.factory.status import StatusEmbedFactory


class Status(AbstractOperation):
    MY_INDEX: str = "status"
    IS_AUTHORIZATION_NEEDED: bool = False

    def __init__(self, message: Message, context: Dict):
        self.__message: Message = message
        self.__context: Dict = context

    def is_authorized(self) -> bool:
        return True

    async def execute(self):
        if len(self.__context["divided"]) != 3:
            embed: Embed = IncorrectCommandEmbedFactory().make()
            await self.__message.channel.send(embed=embed)
            return

        instance_name: str = self.__context["divided"][2]

        try:
            instance: GCEInstanceRepresentingWrapper = GCEClient().get_instance(name=instance_name)
        except InstanceNotFound:
            embed: Embed = InstanceNotFoundEmbedFactory(
                instance_name=instance_name
            ).make()
        else:
            embed: Embed = StatusEmbedFactory(
                instance=instance
            ).make()

        await self.__message.channel.send(embed=embed)
