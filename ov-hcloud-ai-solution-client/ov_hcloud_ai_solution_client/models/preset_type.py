from enum import Enum


class PresetType(str, Enum):
    APP = "app"
    JOB = "job"
    NOTEBOOK = "notebook"

    def __str__(self) -> str:
        return str(self.value)
