from typing import Union, List, Dict

from discord import Embed

from src.discord.embed.factory.base.info import InfoEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class InfoEmbedFactory(InfoEmbedFactoryBase):
    def __init__(
            self,
            title: str,
            detail: str,
            footer: str,
            fields: List[Dict[str, Union[str, bool]]] = None
    ):
        self.__title: str = title
        self.__detail: str = detail
        self.__footer: str = footer
        self.__fields: List[Dict[str, str]] = fields

    def make(self) -> Embed:
        embed = create_embed(
            title=self.__title,
            description=self.__detail,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=self.__footer,
            fields=self.__fields
        )

        return embed
