import os
import base64

from src.config import GCP_ACCOUNT_BASE64, GCP_ACCOUNT_FILE_NAME


def gcp_authenticate():
    target_path = os.getcwd() + "/" + GCP_ACCOUNT_FILE_NAME

    with open(target_path, "w+") as f:
        f.write(base64.b64decode(GCP_ACCOUNT_BASE64).decode(encoding="UTF-8"))

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = target_path
