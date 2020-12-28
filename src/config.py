from typing import List
import os

import discord

DISCORD_TOKEN: str = os.environ["GCPDISCORD_DISCORD_TOKEN"]

DISCORD_INTENTS = discord.Intents.all()
DISCORD_INTENTS.members = True

GCP_ACCOUNT_BASE64: str = os.environ["GCPDISCORD_GCP_ACCOUNT_B64"]
GCP_ACCOUNT_PATH: str = "~/.gcpdiscord_secret.json"

SERVICE_ACCOUNT_ID: str = os.environ["GCPDISCORD_GCP_SERVICE_ACCOUNT_ID"]
GCP_PROJECT_NAME: str = os.environ["GCPDISCORD_GCP_PROJECT_NAME"]
TARGET_INSTANCE_NAME: str = os.environ["GCPDISCORD_GCP_INSTANCE_NAME"]
TARGET_INSTANCE_ZONE: str = os.environ["GCPDISCORD_GCP_INSTANCE_ZONE"]

PERMITTED_ROLE_IDS_STR: List[str] = os.environ["GCPDISCORD_PERMITTED_ROLE_IDS"].split("@")
PERMITTED_ROLE_IDS: List[int] = list(map((lambda element: int(element)), PERMITTED_ROLE_IDS_STR))

PERMISSION_DENIED_MESSAGE: str = "***PERMISSION DENIED!***" \
                            "You are not permitted to use this command. " \
                            "Please contact to your server master."
ERROR_OCCURRED_MESSAGE: str = "***ERROR OCCURRED!***" \
                              "Error has occurred while executing gcp request command." \
                              "Please contact to your server master or software developer." \
                              "Error: {}"

# MAKE SURE SPECIFIED PREFIX IS LOWERCASE
COMMAND_PREFIX: str = "!gcp".lower()
