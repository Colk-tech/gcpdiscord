from discord import Embed

from config import COMMAND_PREFIX
from src.discord.embed.factory.base.error import ErrorEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class UnauthorizedEmbedFactory(ErrorEmbedFactoryBase):
    _TITLE: str = "権限がありません"
    _DETAIL: str = "GCE の操作に必要なロールがついていませんでした"

    def make(self) -> Embed:
        FOOTER: str = f"`{COMMAND_PREFIX}" " " "{start | stop} ${instance_name}" "` " "でインスタンスを操作できます"

        embed = create_embed(
            title=self._TITLE,
            description=self._DETAIL,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=FOOTER,
        )

        return embed
