from typing import Dict

from discord import Message, Embed

from src.gce.client import GCEClient
from src.gce.type.instance import GCEInstanceRepresentingWrapper
from src.gce.exception.gce import InstanceNotFound, OperationFailed

from src.discord.operations.util.authorized import is_authorized_member

from src.discord.operations.abs import AbstractOperation
from src.discord.embed.factory.incorrect_command import IncorrectCommandEmbedFactory
from src.discord.embed.factory.unauthorized import UnauthorizedEmbedFactory
from src.discord.embed.factory.starting_operation import StartingOperation
from src.discord.embed.factory.operation_succeed import OperationSucceedFactory
from src.discord.embed.factory.not_found import InstanceNotFoundEmbedFactory
from src.discord.embed.factory.operation_failed import OperationFailedEmbedFactory

OPERATION_NAME: str = "起動"


class Start(AbstractOperation):
    MY_INDEX: str = "start"
    IS_AUTHORIZATION_NEEDED: bool = False

    def __init__(self, message: Message, context: Dict):
        self.__message: Message = message
        self.__context: Dict = context

    def is_authorized(self) -> bool:
        return is_authorized_member(member=self.__message.author)

    async def execute(self):
        if len(self.__context["divided"]) != 3:
            embed: Embed = IncorrectCommandEmbedFactory().make()
            await self.__message.channel.send(embed=embed)
            return

        instance_name: str = self.__context["divided"][2]

        if not self.is_authorized():
            embed: Embed = UnauthorizedEmbedFactory().make()
            await self.__message.channel.send(embed=embed)
            return

        try:
            instance: GCEInstanceRepresentingWrapper = GCEClient().get_instance(name=instance_name)
        except InstanceNotFound:
            embed: Embed = InstanceNotFoundEmbedFactory(
                instance_name=instance_name
            ).make()

        else:
            embed: Embed = StartingOperation(
                instance_name=instance_name,
                target_state="RUNNING"
            ).make()
            await self.__message.channel.send(embed=embed)

            try:
                GCEClient().start_instance(instance)
            except OperationFailed:
                embed: Embed = OperationFailedEmbedFactory(
                    instance_name=instance_name,
                    operation_name=OPERATION_NAME
                ).make()
            else:
                embed: Embed = OperationSucceedFactory(
                    instance_name=instance_name,
                    after_state="RUNNING"
                ).make()

        await self.__message.channel.send(embed=embed)
