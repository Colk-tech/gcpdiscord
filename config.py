from typing import List
import os

import discord

DISCORD_TOKEN: str = os.environ["GCPDISCORD_DISCORD_TOKEN"]

GCP_ACCOUNT_BASE64: str = os.environ["GCPDISCORD_GCP_ACCOUNT_B64"]
GCP_ACCOUNT_FILE_NAME: str = "gcpdiscord_secret.json"
GCP_ACCOUNT_FILE_PATH: str = os.getcwd() + "/" + GCP_ACCOUNT_FILE_NAME

DISCORD_INTENTS = discord.Intents.all()
DISCORD_INTENTS.members = True

COMMAND_PREFIX: str = "!gcp".lower()
DISCORD_MAIN_CHANNEL_ID: int = int(os.environ["GCPDISCORD_DISCORD_MAIN_CH_ID"])
PERMITTED_ROLE_IDS_STR_LIST: List[str] = os.environ["GCPDISCORD_PERMITTED_ROLE_IDS"].split("@")
PERMITTED_ROLE_IDS: List[int] = list(map((lambda element: int(element)), PERMITTED_ROLE_IDS_STR_LIST))

GCP_PROJECT_NAME: str = os.environ["GCPDISCORD_GCP_PROJECT_NAME"]
GCP_TARGET_INSTANCE_NAME: str = os.environ["GCPDISCORD_GCP_INSTANCE_NAME"]
GCP_TARGET_INSTANCE_ZONE: str = os.environ["GCPDISCORD_GCP_INSTANCE_ZONE"]

MESSAGE_FILE_NAME: str = os.environ["GCPDISCORD_MESSAGE_FILE_NAME"]
MESSAGE_FILE_PATH: str = os.getcwd() + "/messages/" + MESSAGE_FILE_NAME
