from discord import Embed

from src.discord.embed.factory.base.error import ErrorEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class OperationFailedEmbedFactory(ErrorEmbedFactoryBase):
    _TITLE: str = "操作に失敗しました"
    _FOOTER: str = "管理者に問い合わせてください"

    def __init__(self, instance_name: str, operation_name: str):
        self.__instance_name: str = instance_name
        self.__operation_name: str = operation_name

    def make(self) -> Embed:
        DESCRIPTION: str = f"`{self.__instance_name}` の{self.__operation_name}に失敗しました\n" \
                           "しばらく経ってから再試行してください"
        embed = create_embed(
            title=self._TITLE,
            description=DESCRIPTION,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=self._FOOTER,
        )

        return embed
