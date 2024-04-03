from enum import Enum


class ScalingResourceType(str, Enum):
    CPU = "CPU"
    RAM = "RAM"

    def __str__(self) -> str:
        return str(self.value)
