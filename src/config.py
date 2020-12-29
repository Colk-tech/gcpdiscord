from typing import List
import os

import discord

DISCORD_TOKEN: str = os.environ["GCPDISCORD_DISCORD_TOKEN"]

DISCORD_INTENTS = discord.Intents.all()
DISCORD_INTENTS.members = True

DISCORD_MAIN_CHANNEL_ID: int = int(os.environ["GCPDISCORD_DISCORD_MAIN_CH_ID"])

GCP_ACCOUNT_BASE64: str = os.environ["GCPDISCORD_GCP_ACCOUNT_B64"]
GCP_ACCOUNT_FILE_NAME: str = "gcpdiscord_secret.json"
GCP_ACCOUNT_FILE_PATH: str = os.getcwd() + "/" + GCP_ACCOUNT_FILE_NAME

SERVICE_ACCOUNT_ID: str = os.environ["GCPDISCORD_GCP_SERVICE_ACCOUNT_ID"]
GCP_PROJECT_NAME: str = os.environ["GCPDISCORD_GCP_PROJECT_NAME"]
TARGET_INSTANCE_NAME: str = os.environ["GCPDISCORD_GCP_INSTANCE_NAME"]
TARGET_INSTANCE_ZONE: str = os.environ["GCPDISCORD_GCP_INSTANCE_ZONE"]

PERMITTED_ROLE_IDS_STR: List[str] = os.environ["GCPDISCORD_PERMITTED_ROLE_IDS"].split("@")
PERMITTED_ROLE_IDS: List[int] = list(map((lambda element: int(element)), PERMITTED_ROLE_IDS_STR))

# MAKE SURE SPECIFIED PREFIX IS LOWERCASE
COMMAND_PREFIX: str = "!gcp".lower()
