from enum import Enum


class NOTIFICATION_TYPE(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"
    NONE = "NONE"
