from typing import Union, List, Dict

from discord import Message, Embed

from config import COMMAND_PREFIX
from src.discord.operations.abs import AbstractOperation
from src.discord.embed.factory.info import InfoEmbedFactory


class Help(AbstractOperation):
    MY_INDEX: str = "help"
    IS_AUTHORIZATION_NEEDED: bool = False

    __COMMANDS: List[Dict[str, Union[str, bool]]] = [
        {
            "name": f"`{COMMAND_PREFIX} help`",
            "value": "このヘルプを表示します。",
            "inline": False
        },
        {
            "name": f"`{COMMAND_PREFIX} list`",
            "value": "設定されているゾーン内の全てのインスタンスの状態を取得します。",
            "inline": False
        },
        {
            "name": f"`{COMMAND_PREFIX} status" " "  "${instance_name}`",
            "value": "指定されたインスタンスの状態を取得します。",
            "inline": False
        },
        {
            "name": f"`{COMMAND_PREFIX} start" " "  "${instance_name}`",
            "value": "指定されたインスタンスを開始します。",
            "inline": False
        },
        {
            "name": f"`{COMMAND_PREFIX} stop" " "  "${instance_name}`",
            "value": "指定されたインスタンスを終了します。",
            "inline": False
        }
    ]

    def __init__(self, message: Message, context: Dict):
        self.__message: Message = message
        self.__context: Dict = context

    def is_authorized(self) -> bool:
        return True

    async def execute(self):
        embed: Embed = InfoEmbedFactory(
            title="ヘルプ",
            detail=None,
            footer="Created by: @Colk_",
            fields=self.__COMMANDS
        ).make()

        await self.__message.channel.send(embed=embed)
