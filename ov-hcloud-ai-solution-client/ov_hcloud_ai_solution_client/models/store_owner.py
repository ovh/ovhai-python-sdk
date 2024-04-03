from enum import Enum


class StoreOwner(str, Enum):
    CUSTOMER = "customer"
    OVHCLOUD = "ovhcloud"

    def __str__(self) -> str:
        return str(self.value)
