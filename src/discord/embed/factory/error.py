from discord import Embed

from src.discord.embed.factory.base.error import ErrorEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class ErrorEmbedFactory(ErrorEmbedFactoryBase):
    def __init__(
            self,
            title: str,
            detail: str,
            footer: str = "管理者に問い合わせてください"
    ):
        self.__title: str = title
        self.__detail: str = detail
        self.__footer: str = footer

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
        )

        return embed
