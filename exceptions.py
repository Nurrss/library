class LibraryError(Exception):
    "Базовая ошибка библиотеки — корень дерева."

class ItemNotFound(LibraryError):
    def __init__(self, item_id: int):
        self.item_id = item_id
        super().__init__(f"Предмет с id={item_id} не найден")

class ReaderNotFound(LibraryError):
    def __init__(self, reader_id : int):
        self.reader_id = reader_id
        super().__init__(f"Читатель с {reader_id} не найден")

class ItemNotAvailable(LibraryError):
    def __init__(self, title : str):
        self.title = title
        super().__init__(f"«{title}» сейчас на руках")

class LoanLimitExceeded(LibraryError):
    def __init__(self, reader_name : str , limit : int):
        self.reader_name = reader_name
        self.limit = limit
        super().__init__(f"{reader_name} уже взял(а) максимум — {limit} шт.")

class NotBorrowed(LibraryError):
    def __init__(self, item_id = int):
        self.item_id = item_id
        super().__init__(f"Предмет с {item_id} не выдавался")