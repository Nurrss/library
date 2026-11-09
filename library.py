from datetime import date , timedelta

from enums import ItemStatus, LoanStatus
from models import LibraryItem , Reader, Loan
from exceptions import (
    ItemNotFound, ReaderNotFound, ItemNotAvailable,
    LoanLimitExceeded, NotBorrowed,
)

class Library:
    MAX_LOANS = 2

    def __init__(self) -> None:
        self.items: dict[int, LibraryItem] = {}
        self.readers: dict[int, Reader] = {}
        self.loans: list[Loan] = []

    def _get_item(self, item_id : int) -> LibraryItem:
        try:
            return self.items[item_id]
        except:
            raise ItemNotFound(item_id) from None

    def _get_reader(self, reader_id : int) -> Reader:
        try:
            return self.readers[reader_id]
        except:
            raise ReaderNotFound(reader_id) from None

    def _active_loans_of(self, reader : Reader) -> list[Loan]:
        return [loan for loan in self.loans if loan.reader.id == reader.id and loan.status == LoanStatus.ACTIVE]

    def add_item(self, item: LibraryItem) -> None:
        self.items[item.id] = item

    def add_reader(self, reader: Reader) -> None:
        self.readers[reader.id] = reader

    def checkout(self, item_id: int, reader_id: int) -> Loan:
        item = self._get_item(item_id)
        reader = self._get_reader(reader_id)

        if item.status != ItemStatus.AVAILABLE:
            raise ItemNotAvailable(item.title)

        if(len(self._active_loans_of(reader)) >= self.MAX_LOANS):
            raise LoanLimitExceeded(reader.name, self.MAX_LOANS)

        due = date.today() + timedelta(days=item.loan_days())
        loan = Loan(item, reader, due)

        item.status = ItemStatus.BORROWED
        self.loans.append(loan)
        return loan

    def return_item(self, item_id: int) -> None:
        for loan in self.loans:
            if loan.item.id == item_id and loan.status == LoanStatus.ACTIVE:
                loan.status = LoanStatus.RETURNED
                loan.item.status = ItemStatus.AVAILABLE
                return
        raise NotBorrowed(item_id)

    def available_items(self) -> list[LibraryItem]:
        return [item for item in self.items.values() if item.status == ItemStatus.AVAILABLE]


from contextlib import contextmanager      # ← в начало файла, к остальным импортам


@contextmanager
def transaction(library: Library):
    # ===== ВХОД: «фотографируем» состояние =====
    saved_item_statuses = {item_id: item.status for item_id, item in library.items.items()}
    saved_loan_statuses = [loan.status for loan in library.loans]
    saved_loans_count = len(library.loans)

    try:
        yield library                   # здесь выполняется тело with
    except Exception:
        # ===== ОШИБКА: откатываем по «фотографии» =====
        for item_id, status in saved_item_statuses.items():
            library.items[item_id].status = status

        del library.loans[saved_loans_count:]      # удалить выдачи, созданные внутри with

        # TODO: верните старые статусы выдачам, которые были ДО транзакции
        #       подсказка: zip(library.loans, saved_loan_statuses) даёт пары (loan, status)

        raise                           # ошибку НЕ глотаем — пусть demo.py её обработает