import os
import subprocess
import base64

from src.config import GCP_ACCOUNT_BASE64, GCP_ACCOUNT_FILE_NAME

COMMAND_TEMPLATE = "gcloud auth activate-service-account --key-file {}"


def gcp_authenticate():
    raw_command = COMMAND_TEMPLATE.format(GCP_ACCOUNT_FILE_NAME)

    target_path = os.getcwd() + "/" + GCP_ACCOUNT_FILE_NAME

    with open(target_path, "w+") as f:
        f.write(base64.b64decode(GCP_ACCOUNT_BASE64).decode(encoding="UTF-8"))

    subprocess.call(raw_command.split())
