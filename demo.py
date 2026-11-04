from models import Book, Reader, Magazine, LibraryItem
from enums import ItemStatus

book1 = Book(1, "Абай жолы", "Мухтар Ауэзов")
book2 = Book(2, "Кочевники", "Ильяс Есенберлин")
reader = Reader(1, "Алия")
mag1 = Magazine(3, "National Geographic", 42)

book1.status = ItemStatus.BORROWED

books = [book1, book2]
available = [books[book].title for book in range(len(books)) if books[book].status == ItemStatus.AVAILABLE]
print(available)

items: list[LibraryItem] = [book1, book2, mag1]
for item in items:
    print(f"«{item.title}» выдаётся на {item.loan_days()} дней")

print("--- JSON ---")
print(book1.to_json())
print(mag1.to_json())
print(reader.to_json())