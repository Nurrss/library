from library import Library
from models import Book, Magazine, Reader
from exceptions import LibraryError, ItemNotAvailable

lib = Library()

# ===== 1. Создаём =====
lib.add_item(Book(1, "Абай жолы", "Мухтар Ауэзов"))
lib.add_item(Book(2, "Кочевники", "Ильяс Есенберлин"))
lib.add_item(Magazine(3, "National Geographic", 42))
lib.add_reader(Reader(1, "Алия"))
lib.add_reader(Reader(2, "Ерлан"))

print("Доступно:", [i.title for i in lib.available_items()])

# ===== 2. Выдаём =====
loan = lib.checkout(1, 1)
print(f"Выдано: «{loan.item.title}» → {loan.reader.name}, вернуть до {loan.due}")

loan2 = lib.checkout(3, 2)
print(f"Выдано: «{loan2.item.title}» → {loan2.reader.name}, вернуть до {loan2.due}")

print("Доступно:", [i.title for i in lib.available_items()])

# ===== 3. Возвращаем =====
lib.return_item(1)
print("Вернули книгу 1, статус выдачи:", loan.status.name)
print("Доступно:", [i.title for i in lib.available_items()])

# ===== 4. Ошибки =====
print("\n--- Ошибки ---")

# Выдать то, что уже на руках (журнал у Ерлана)
try:
    lib.checkout(3, 1)
except ItemNotAvailable as e:
    print(f"⚠️ {e}")

# Несуществующая книга
try:
    lib.checkout(999, 1)
except LibraryError as e:
    print(f"⚠️ {type(e).__name__}: {e}")

# Несуществующий читатель
try:
    lib.checkout(2, 777)
except LibraryError as e:
    print(f"⚠️ {type(e).__name__}: {e}")

# Вернуть то, что не выдавалось
try:
    lib.return_item(2)
except LibraryError as e:
    print(f"⚠️ {type(e).__name__}: {e}")

# Лимит: Алия берёт 2 книги, третья — ошибка
lib.add_item(Book(4, "Путь Абая", "Мухтар Ауэзов"))
lib.checkout(1, 1)
lib.checkout(2, 1)
try:
    lib.checkout(4, 1)
except LibraryError as e:
    print(f"⚠️ {type(e).__name__}: {e}")