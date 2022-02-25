from discord import Embed

from config import COMMAND_PREFIX
from src.discord.embed.factory.base.error import ErrorEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class IncorrectCommandEmbedFactory(ErrorEmbedFactoryBase):
    _TITLE: str = "コマンドの形式が間違っています"

    def make(self) -> Embed:
        DESCRIPTION: str = f"`{COMMAND_PREFIX} help` でヘルプを確認して、正しい構文で再試行してください"

        embed = create_embed(
            title=self._TITLE,
            description=DESCRIPTION,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL
        )

        return embed
