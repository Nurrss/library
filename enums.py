from enum import Enum , auto

class ItemStatus():
    AVAILABLE = auto()
    BORROWED = auto()

class LoanStatus():
    ACTIVE = auto()
    RETURNED = auto()
    