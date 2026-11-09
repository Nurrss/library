from abc import ABC , abstractmethod
from mixins import JsonMixin
from dataclasses import dataclass, field
from enums import ItemStatus, LoanStatus
from datetime import date

@dataclass
class LibraryItem(JsonMixin, ABC):
    id: int
    title : str
    status : ItemStatus = field(default=ItemStatus.AVAILABLE, kw_only=True)

    @abstractmethod
    def loan_days(self) -> int:
        "На сколько дней выдаётся."


@dataclass
class Book(LibraryItem):
    author : str

    def loan_days(self) -> int:
        return 14

@dataclass
class Magazine(LibraryItem):
    issue : int

    def loan_days(self):
        return 7

@dataclass
class Reader(JsonMixin):
    id : int
    name : str


@dataclass 
class Loan:
    item : LibraryItem
    reader : Reader
    due : date
    status : LoanStatus = LoanStatus.ACTIVE