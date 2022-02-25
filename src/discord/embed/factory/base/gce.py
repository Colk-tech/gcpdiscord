from src.discord.embed.factory.base.author import AbstractEmbedFactory

from config import (
    GCE_ICON_URL
)


class GCEEmbedFactoryBase(AbstractEmbedFactory):
    _EMBED_COLOR: int = 0x185ae1
    _AUTHOR_NAME: str = "GCE VM ダッシュボード"
    _AUTHOR_URL: str = 'https://console.cloud.google.com/compute/instances'
    _AUTHOR_ICON_URL: str = GCE_ICON_URL
    _THUMBNAIL_URL: str = GCE_ICON_URL
