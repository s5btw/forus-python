from db.crud import get_books, get_categories
from db.db import get_session

session = get_session()

try:
    categories = get_categories(session)

    print("Категории:")

    for category in categories:
        print(f"{category.id}. {category.title}")

    print()
    print("Книги:")

    books = get_books(session)

    for book in books:
        print(f"{book.id}. {book.title}")
        print(f"   Описание: {book.description}")
        print(f"   Цена: {book.price}")
        print(f"   Категория: {book.category.title}")
        print()
finally:
    session.close()