from enum import Enum


class MeTokenKind(str, Enum):
    APP = "app"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
