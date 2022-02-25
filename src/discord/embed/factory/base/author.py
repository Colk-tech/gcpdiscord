from config import (
    MY_NAME,
    GCE_ICON_URL
)
from src.discord.embed.factory.base.abs import AbstractEmbedFactory


class AuthorEmbedFactoryBase(AbstractEmbedFactory):
    _AUTHOR_NAME: str = MY_NAME
    _AUTHOR_URL: str = GCE_ICON_URL
    _AUTHOR_ICON_URL: str = GCE_ICON_URL
