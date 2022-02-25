from typing import Dict

import google.cloud.compute_v1.types.compute

RUNNING_ICON: str = "O"
TERMINATED_ICON: str = "X"
UNKNOWN_ICON: str = "?"
RUNNING_TRANSLATED: str = "稼働中"
TERMINATED_TRANSLATED: str = "停止中"
UNKNOWN_TRANSLATED: str = "不明"


class GCEInstanceRepresentingWrapper:
    def __init__(self, instance: google.cloud.compute_v1.types.compute.Instance):
        self.__MY_INSTANCE: google.cloud.compute_v1.types.compute.Instance = instance

    @property
    def id(self) -> str:
        return self.__MY_INSTANCE.id

    @property
    def name(self) -> str:
        return self.__MY_INSTANCE.name

    @property
    def description(self) -> str:
        return self.__MY_INSTANCE.description

    @property
    def zone(self) -> str:
        return self.__MY_INSTANCE.zone

    @property
    def status(self) -> str:
        return self.__MY_INSTANCE.status

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "zone": self.zone,
            "status": self.status
        }

    def get_status_icon(self) -> str:
        if self.status == "RUNNING":
            return RUNNING_ICON

        if self.status == "TERMINATED":
            return TERMINATED_ICON

        return UNKNOWN_ICON

    def get_translated_status(self) -> str:
        if self.status == "RUNNING":
            return RUNNING_TRANSLATED

        if self.status == "TERMINATED":
            return TERMINATED_TRANSLATED

        return RUNNING_TRANSLATED

    def __repr__(self):
        return f"\"{self.name}\" <{self.id}>"
