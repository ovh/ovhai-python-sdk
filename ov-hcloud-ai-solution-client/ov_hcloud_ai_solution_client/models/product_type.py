from enum import Enum


class ProductType(str, Enum):
    APP = "app"
    JOB = "job"
    NOTEBOOK = "notebook"

    def __str__(self) -> str:
        return str(self.value)
