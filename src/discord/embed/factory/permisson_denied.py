from discord import Embed

from src.discord.embed.factory.base.error import ErrorEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class PermissionDeniedEmbedFactory(ErrorEmbedFactoryBase):
    _TITLE: str = "必要な権限がありません"
    _DESCRIPTION: str = "あなたには GCE を操作するためのロールが付与されていません"
    _FOOTER: str = "管理者に問い合わせてください"

    def make(self) -> Embed:
        embed = create_embed(
            title=self._TITLE,
            description=self._DESCRIPTION,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=self._FOOTER,
        )

        return embed
