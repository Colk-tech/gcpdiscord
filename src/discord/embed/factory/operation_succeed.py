from discord import Embed

from src.discord.embed.factory.base.info import InfoEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class OperationSucceedFactory(InfoEmbedFactoryBase):
    def __init__(self, instance_name, after_state: str):
        self.__instance_name: str = instance_name
        self.__after_state: str = after_state

    def make(self) -> Embed:
        title: str = str()
        color: int = int()
        footer: str = str()

        if self.__after_state == "RUNNING":
            title: str = f"{self.__instance_name} は正常に起動しました"
            color: int = 0x18702a
            footer: str = "使い終わったら切ってくださいね"

        if self.__after_state == "TERMINATED":
            title: str = f"{self.__instance_name} は正常に停止しました"
            color: int = 0x414244
            footer: str = "次回も Discord から起動できます"

        embed = create_embed(
            title=title,
            color=color,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=footer,
        )

        return embed
