from typing import List
import os

import discord

DISCORD_TOKEN: str = os.environ["GCEDISCORD_DISCORD_TOKEN"]

DISCORD_INTENTS = discord.Intents.all()
DISCORD_INTENTS.members = True

COMMAND_PREFIX: str = "!gce"

DISCORD_MAIN_CHANNEL_ID: int = int(os.environ["GCEDISCORD_DISCORD_MAIN_CH_ID"])
PERMITTED_ROLE_IDS: List[int] = [int(element) for element in
                                 os.environ["GCEDISCORD_PERMITTED_ROLE_IDS"].split("@")]

GCE_ACCOUNT_FILE_PATH: str = os.path.abspath(os.path.dirname(__file__)) + "/" + "gcediscord_secret.json"

GCE_TARGET_INSTANCE_ZONE: str = os.environ["GCEDISCORD_GCE_INSTANCE_ZONE"]

MY_NAME: str = "GCE Controller"
GCE_ICON_URL: str = "https://download.logo.wine/logo/Google_Compute_Engine/Google_Compute_Engine-Logo.wine.png"
