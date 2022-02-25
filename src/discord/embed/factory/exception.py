from discord import Embed

from src.discord.embed.factory.base.error import ErrorEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class ExceptionEmbedFactory(ErrorEmbedFactoryBase):
    _TITLE: str = "不明なエラーが発生しました"
    _FOOTER: str = "管理者に問い合わせてください"

    def __init__(self, exception: Exception):
        self.__exception = exception

    def make(self) -> Embed:
        description: str = "例外の内容:\n" \
                           f"{type(self.__exception)}:\n" \
                           "```\n" \
                           f"{self.__exception}\n" \
                           "```"

        embed = create_embed(
            title=self._TITLE,
            description=description,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=self._FOOTER,
        )

        return embed
