import time

from googleapiclient.discovery import build, Resource
from oauth2client.client import GoogleCredentials

from src.config import (
    GCP_PROJECT_NAME,
    TARGET_INSTANCE_NAME,
    TARGET_INSTANCE_ZONE
)


class GCPCommandRequest:
    IS_CONFIGURED = False

    @classmethod
    def config_from_param(
            cls,
            gcp_project_name: str,
            target_instance_name: str,
            target_instance_zone: str
    ):
        cls.gcp_project_name: str = gcp_project_name
        cls.target_instance_name: str = target_instance_name
        cls.target_instance_zone: str = target_instance_zone

        google_credential = cls.create_google_credential()
        cls.compute: Resource = build("compute", "v1", credentials=google_credential)

        cls.IS_CONFIGURED = True

    @classmethod
    def config_from_environ(cls):
        cls.config_from_param(
            GCP_PROJECT_NAME,
            TARGET_INSTANCE_NAME,
            TARGET_INSTANCE_ZONE
        )

    def __init__(self, operation: str):
        cls = GCPCommandRequest

        if not cls.IS_CONFIGURED:
            cls.config_from_environ()

        self.operation: str = operation.lower()
        self.execute()

    def execute(self) -> None:
        cls = GCPCommandRequest

        cls.check_configured()

        instance_status = "RUNNING" if self.operation == "start" else "TERMINATED"

        if self.operation == "start":
            result: dict = cls.compute.instances().start(
                project=cls.gcp_project_name,
                zone=cls.target_instance_zone,
                instance=cls.target_instance_name
            ).execute()
        if self.operation == "stop":
            result: dict = cls.compute.instances().stop(
                project=cls.gcp_project_name,
                zone=cls.target_instance_zone,
                instance=cls.target_instance_name
            ).execute()

        challenging_times = 0
        while True:
            challenging_times += 1
            instance: dict = cls.compute.instances().get(
                project=cls.gcp_project_name,
                zone=cls.target_instance_zone,
                instance=cls.target_instance_name
            ).execute()
            if instance["status"] == instance_status:
                return
            if challenging_times >= 60:
                raise RuntimeError(f"Failed to {self.operation} the instance."
                                   f"Though we waited for 3 minutes to start the GCP instance, it has not started yet.")
            time.sleep(3)

    @staticmethod
    def create_google_credential() -> GoogleCredentials:
        credentials: GoogleCredentials = GoogleCredentials.get_application_default()
        return credentials

    @classmethod
    def check_configured(cls):
        if not cls.IS_CONFIGURED:
            raise RuntimeError("Please make sure you have created instance of this class first.")

    def check_already_in_status_of(self, operation: str) -> bool:
        cls = GCPCommandRequest

        instance_status = "RUNNING" if operation == "start" else "TERMINATED"

        instance: dict = cls.compute.instances().get(
            project=cls.gcp_project_name,
            zone=cls.target_instance_zone,
            instance=cls.target_instance_name
        ).execute()

        if instance["status"] == instance_status:
            return True

        return False
