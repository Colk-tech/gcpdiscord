import subprocess
import base64

from src.config import GCP_ACCOUNT_BASE64, GCP_ACCOUNT_PATH

COMMAND_TEMPLATE = "gcloud auth activate-service-account --key-file {}"


def gcp_authenticate():
    raw_command = COMMAND_TEMPLATE.format(GCP_ACCOUNT_PATH)

    with open(GCP_ACCOUNT_PATH, "wb") as f:
        f.write(base64.b64decode(GCP_ACCOUNT_BASE64))

    subprocess.call(raw_command.split())
