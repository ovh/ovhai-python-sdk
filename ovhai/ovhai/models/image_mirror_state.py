from enum import Enum


class ImageMirrorState(str, Enum):
    DELETED = "DELETED"
    DELETING = "DELETING"
    DONE = "DONE"
    ERROR = "ERROR"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
