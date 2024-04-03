from enum import Enum


class Role(str, Enum):
    ADMINISTRATOR = "administrator"
    AI_TRAINING_OPERATOR = "ai_training_operator"
    AI_TRAINING_READ = "ai_training_read"

    def __str__(self) -> str:
        return str(self.value)
