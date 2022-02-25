from discord import Embed

from src.discord.embed.factory.base.error import ErrorEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class InstanceNotFoundEmbedFactory(ErrorEmbedFactoryBase):
    _TITLE: str = "インスタンスが見つかりませんでした"

    def __init__(self, instance_name: str):
        self.__instance_name: str = instance_name

    def make(self) -> Embed:
        detail: str = f"指定されたインスタンス {self.__instance_name} が見つかりませんでした\n" \
                      "インスタンス名が正しいことを確認してもう一度試してください"

        embed = create_embed(
            title=self._TITLE,
            description=detail,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL
        )

        return embed
