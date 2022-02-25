from typing import Union, List, Dict

from discord import Embed

from src.util.remove_none_arguments import remove_none_arguments


def create_embed(
        title: str = None,
        description: str = None,
        url: str = None,
        color: int = None,
        author_name: str = None,
        author_url: str = None,
        author_icon_url: str = None,
        thumbnail_url: str = None,
        footer: str = None,
        fields: List[Dict[str, Union[str, bool]]] = None,
) -> Embed:
    args: Dict = remove_none_arguments(
        title=title,
        description=description,
        url=url,
        color=color,
    )[1]
    composing: Embed = Embed(**args)

    args: Dict = remove_none_arguments(
        name=author_name,
        url=author_url,
        icon_url=author_icon_url
    )[1]
    if args:
        composing.set_author(
            **args
        )

    if thumbnail_url:
        composing.set_thumbnail(
            url=thumbnail_url
        )

    if footer:
        composing.set_footer(
            text=footer
        )

    if fields:
        for elem in fields:
            elem.setdefault("inline", False)

            composing.add_field(
                name=elem["name"],
                value=elem["value"],
                inline=elem["inline"]
            )

    return composing
