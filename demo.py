from models import Book, Reader
from enums import ItemStatus

book1 = Book(1, "Абай жолы", "Мухтар Ауэзов")
book2 = Book(2, "Кочевники", "Ильяс Есенберлин")
reader = Reader(1, "Алия")

book1.status = ItemStatus.BORROWED

books = [book1, book2]
available = [books[book].title for book in range(len(books)) if books[book].status == ItemStatus.AVAILABLE]
print(available)
