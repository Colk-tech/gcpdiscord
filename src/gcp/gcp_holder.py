
import os
import base64

from config import GCP_ACCOUNT_BASE64, GCP_ACCOUNT_FILE_NAME, GCP_PROJECT_NAME, GCP_TARGET_INSTANCE_NAME, GCP_TARGET_INSTANCE_ZONE

from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build, Resource
from src.utils.singleton import Singleton


class GCPHolder(Singleton):
    def __init__(self):
        self.CREDENTIAL: GoogleCredentials = self.get_gcp_credential()
        self.RESOURCE: Resource = build("compute", "v1", credentials=self.CREDENTIAL)
        self.INSTANCE = self.__get_instance()

    def __get_instance(self):
        instance = self.RESOURCE.instances().get(
            project=GCP_PROJECT_NAME,
            zone=GCP_TARGET_INSTANCE_ZONE,
            instance=GCP_TARGET_INSTANCE_NAME
        ).execute()
        return instance

    @staticmethod
    def get_gcp_credential() -> GoogleCredentials:
        target_path = os.getcwd() + "/" + GCP_ACCOUNT_FILE_NAME

        with open(target_path, "w+") as f:
            f.write(base64.b64decode(GCP_ACCOUNT_BASE64).decode(encoding="UTF-8"))

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = target_path

        credential: GoogleCredentials = GoogleCredentials.get_application_default()

        return credential
