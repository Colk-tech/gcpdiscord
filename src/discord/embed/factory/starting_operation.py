from discord import Embed

from src.discord.embed.factory.base.info import InfoEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class StartingOperation(InfoEmbedFactoryBase):
    _FOOTER: str = "これには数分かかることがあります..."

    def __init__(self, instance_name, target_state: str):
        self.__instance_name: str = instance_name
        self.__target_state: str = target_state

    def make(self) -> Embed:
        title: str = str()

        if self.__target_state == "RUNNING":
            title: str = f"{self.__instance_name} を開始しています..."

        if self.__target_state == "TERMINATED":
            title: str = f"{self.__instance_name} を停止しています..."

        embed = create_embed(
            title=title,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=self._FOOTER,
        )

        return embed
