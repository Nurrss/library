from enum import Enum , auto

class ItemStatus(Enum):
    AVAILABLE = auto()
    BORROWED = auto()

class LoanStatus(Enum):
    ACTIVE = auto()
    RETURNED = auto()
