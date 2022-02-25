from typing import Union, List, Dict

from discord import Embed

from config import (
    COMMAND_PREFIX,
    GCE_TARGET_INSTANCE_ZONE
)
from src.discord.embed.factory.base.gce import GCEEmbedFactoryBase
from src.discord.embed.util.create_embed import create_embed
from src.gce.type.instance import GCEInstanceRepresentingWrapper


class InstanceListEmbedFactory(GCEEmbedFactoryBase):
    def __init__(
            self,
            instances: List[GCEInstanceRepresentingWrapper],
            zone: str = GCE_TARGET_INSTANCE_ZONE
    ):
        self.__instances: List[GCEInstanceRepresentingWrapper] = instances
        self.__zone: str = zone

    def _get_fields(self) -> List[Dict[str, Union[str, bool]]]:
        fields: List[Dict[str, Union[str, bool]]] = list()

        for instance in self.__instances:
            fields.append(
                {
                    "name": f"{instance.get_status_icon()}: `{instance.name}`",
                    "value": f"**{instance.status}**",
                    "inline": False
                }
            )

        return fields

    def make(self) -> Embed:
        FOOTER: str = f"`{COMMAND_PREFIX}" " " "{start | stop} ${instance_name}" "` " "でインスタンスを操作できます"

        title: str = f'"{self.__zone}" にあるインスタンスの一覧'
        fields: List[Dict[str, Union[str, bool]]] = self._get_fields()

        embed = create_embed(
            title=title,
            color=self._EMBED_COLOR,
            author_name=self._AUTHOR_NAME,
            author_url=self._AUTHOR_URL,
            author_icon_url=self._AUTHOR_ICON_URL,
            thumbnail_url=self._THUMBNAIL_URL,
            footer=FOOTER,
            fields=fields
        )

        return embed
