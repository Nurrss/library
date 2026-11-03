from abc import ABC , abstractmethod
from dataclasses import dataclass, field
from enums import ItemStatus

@dataclass
class LibraryItem(ABC):
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
class Reader():
    id : int
    name : str
