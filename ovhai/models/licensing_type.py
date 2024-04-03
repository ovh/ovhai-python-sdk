from enum import Enum


class LicensingType(str, Enum):
    PER_APP = "per-app"
    PER_REPLICA = "per-replica"
    PER_RESOURCE = "per-resource"
    PER_SECOND_BRACKET = "per-second-bracket"

    def __str__(self) -> str:
        return str(self.value)
