from app.db.models import Book, Category


def create_category(session, title):
    category = Category(title=title)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


def get_categories(session):
    return session.query(Category).all()


def get_category(session, category_id):
    return session.query(Category).filter(Category.id == category_id).first()


def update_category(session, category_id, title):
    category = get_category(session, category_id)

    if category is None:
        return None

    category.title = title
    session.commit()
    session.refresh(category)
    return category


def delete_category(session, category_id):
    category = get_category(session, category_id)

    if category is None:
        return False

    session.delete(category)
    session.commit()
    return True


def create_book(session, title, description, price, url, category_id):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )

    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_books(session, category_id=None):
    query = session.query(Book)

    if category_id is not None:
        query = query.filter(Book.category_id == category_id)

    return query.all()


def get_book(session, book_id):
    return session.query(Book).filter(Book.id == book_id).first()


def update_book(session, book_id, title=None, description=None, price=None, url=None, category_id=None):
    book = get_book(session, book_id)

    if book is None:
        return None

    if title is not None:
        book.title = title

    if description is not None:
        book.description = description

    if price is not None:
        book.price = price

    if url is not None:
        book.url = url

    if category_id is not None:
        book.category_id = category_id

    session.commit()
    session.refresh(book)
    return book


def delete_book(session, book_id):
    book = get_book(session, book_id)

    if book is None:
        return False

    session.delete(book)
    session.commit()
    return True
