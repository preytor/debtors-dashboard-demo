from enum import Enum

class PaymentStatusEnum(Enum):
    ON_TIME = "On time"
    LATE = "Late"
    MISSED = "Missed"