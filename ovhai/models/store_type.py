from enum import Enum


class StoreType(str, Enum):
    GIT = "git"
    S3 = "s3"
    SWIFT = "swift"

    def __str__(self) -> str:
        return str(self.value)
