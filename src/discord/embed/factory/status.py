from discord import Embed

from config import GCE_TARGET_INSTANCE_ZONE

from src.gce.type.instance import GCEInstanceRepresentingWrapper

from config import COMMAND_PREFIX
from src.discord.embed.factory.base.gce import GCEEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed


class StatusEmbedFactory(GCEEmbedFactoryBase):
    def __init__(
            self,
            instance: GCEInstanceRepresentingWrapper,
            zone: str = GCE_TARGET_INSTANCE_ZONE
    ):
        self.__instance: GCEInstanceRepresentingWrapper = instance
        self.__zone: str = zone

    def make(self) -> Embed:
        AUTHOR_URL: str = "https://console.cloud.google.com/compute/instancesDetail/zones/" \
                          f"{self.__zone}/instances/{self.__instance.name}"
        FOOTER: str = f"`{COMMAND_PREFIX}" " " "{start | stop} ${instance_name}" "` " "でインスタンスを操作できます"

        title: str = f'"{self.__instance.name}" の状態'
        description: str = f"{self.__instance.get_status_icon()} " \
                           f"{self.__instance.get_translated_status()} " \
                           f"({self.__instance.status})"

        embed = create_embed(
            title=title,
            description=description,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=FOOTER
        )

        return embed
