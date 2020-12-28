from typing import List

import subprocess

from src.config import SERVICE_ACCOUNT_ID, GCP_PROJECT_NAME, TARGET_INSTANCE_NAME, TARGET_INSTANCE_ZONE


class GCPCommandRequest:
    IS_CONFIGURED = False
    COMMAND_TEMPLATE = "/snap/bin/gcloud --account={} compute instances {} {} --project {} --zone {}"
    # f"/snap/bin/gcloud --account={SERVICE_ACCOUNT_ID} compute instances {option} {MINECRAFT_INSTANCE_NAME} \
    # --project {GCP_PROJECT_NAME} --zone {MINECRAFT_INSTANCE_ZONE}"

    @classmethod
    def config_from_param(
            cls,
            service_account_id: str,
            gcp_project_name: str,
            target_instance_name: str,
            target_instance_zone: str
    ):
        cls.service_account_id = service_account_id
        cls.gcp_project_name = gcp_project_name
        cls.target_instance_name = target_instance_name
        cls.target_instance_zone = target_instance_zone
        cls.IS_CONFIGURED = True

    @classmethod
    def config_from_environ(cls):
        cls.config_from_param(SERVICE_ACCOUNT_ID, GCP_PROJECT_NAME, TARGET_INSTANCE_NAME, TARGET_INSTANCE_ZONE)

    def __init__(self, operation: str):
        cls = GCPCommandRequest

        if not cls.IS_CONFIGURED:
            cls.config_from_environ()

        self.operation: str = operation
        self.command: List[str] = self.create_command()

    def create_command(self) -> List[str]:
        cls = GCPCommandRequest

        raw_command = cls.COMMAND_TEMPLATE.format(
            cls.service_account_id,
            self.operation,
            cls.target_instance_name,
            cls.gcp_project_name,
            cls.target_instance_zone
        )

        return raw_command.split()

    def execute(self):
        subprocess.call(self.command)
