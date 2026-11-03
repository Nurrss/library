from models import Book, Reader

book1 = Book(1, "Абай жолы", "Мухтар Ауэзов")
book2 = Book(2, "Кочевники", "Ильяс Есенберлин")
reader = Reader(1, "Алия")

print(book1)
print(book2)
print(reader)
print(book1.title, "—", book1.author)
print(book1 == Book(1, "Абай жолы", "Мухтар Ауэзов"))