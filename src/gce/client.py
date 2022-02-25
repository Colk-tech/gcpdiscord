from typing import Tuple, List, Optional

import google.auth
import google.cloud.compute_v1

from src.util.singleton import Singleton

from src.gce.exception.gce import InstanceNotFound, OperationFailed

from src.gce.type.instance import GCEInstanceRepresentingWrapper

from config import (
    GCE_ACCOUNT_FILE_PATH,
    GCE_TARGET_INSTANCE_ZONE
)

OPERATION_CHALLENGE_TIMES = 9
OPERATION_RETRY_INTERVAL = 10


def _authenticate() -> Tuple[google.auth.credentials.Credentials, Optional[str]]:
    credentials, project = google.auth.load_credentials_from_file(filename=GCE_ACCOUNT_FILE_PATH)

    return credentials, project


def _get_client(credentials: google.auth.credentials.Credentials) -> \
        google.cloud.compute_v1.services.instances.InstancesClient:
    client = google.cloud.compute_v1.services.instances.InstancesClient(
        credentials=credentials
    )

    return client


class GCEClient(Singleton):
    __authenticate_result: Tuple[google.auth.credentials.Credentials, Optional[str]] = _authenticate()
    __CREDENTIALS: google.auth.credentials.Credentials = __authenticate_result[0]
    __PROJECT: google.auth.credentials.Credentials = __authenticate_result[1]
    __CLIENT: google.cloud.compute_v1.services.instances.InstancesClient = _get_client(__CREDENTIALS)

    def __init__(self):
        pass

    def __get_raw_instances(self,
                            project: str,
                            zone: str) -> google.cloud.compute_v1.services.instances.pagers.ListPager:
        return self.__CLIENT.list(
            project=project,
            zone=zone,
        )

    def get_instances(self, zone: str = GCE_TARGET_INSTANCE_ZONE) -> List[GCEInstanceRepresentingWrapper]:
        raw_instances = self.__get_raw_instances(
            project=self.__PROJECT,
            zone=zone
        )

        retval: List[GCEInstanceRepresentingWrapper] = [
            GCEInstanceRepresentingWrapper(instance=raw_instance) for raw_instance in raw_instances
        ]

        return retval

    def get_instance(self, name: str) -> GCEInstanceRepresentingWrapper:
        try:
            raw_instance = self.__CLIENT.get(
                project=self.__PROJECT,
                zone=GCE_TARGET_INSTANCE_ZONE,
                instance=name,
            )

            instance = GCEInstanceRepresentingWrapper(instance=raw_instance)

        except google.api_core.exceptions.NotFound:
            raise InstanceNotFound()

        return instance

    def is_instance_exists(self, name: str) -> bool:
        try:
            self.get_instance(name=name)

        except InstanceNotFound:
            return False

        return True

    def start_instance(self, target: GCEInstanceRepresentingWrapper):
        challenging_times = 0

        while target.status != "RUNNING":
            if challenging_times > OPERATION_CHALLENGE_TIMES:
                raise OperationFailed()

            else:
                challenging_times += 1

                self.__CLIENT.start_unary(
                    project=self.__PROJECT,
                    zone=GCE_TARGET_INSTANCE_ZONE,
                    instance=target.name
                )

            target: GCEInstanceRepresentingWrapper = self.get_instance(target.name)

    def stop_instance(self, target: GCEInstanceRepresentingWrapper):
        challenging_times = 0

        while target.status != "TERMINATED":
            if challenging_times > OPERATION_CHALLENGE_TIMES:
                raise OperationFailed()

            else:
                challenging_times += 1

                self.__CLIENT.stop_unary(
                    project=self.__PROJECT,
                    zone=GCE_TARGET_INSTANCE_ZONE,
                    instance=target.name
                )

            target: GCEInstanceRepresentingWrapper = self.get_instance(target.name)
