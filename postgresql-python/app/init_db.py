from db.crud import create_book, create_category
from db.db import engine, get_session
from db.models import Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

session = get_session()

try:
    programming = create_category(session, "Программирование")
    databases = create_category(session, "Базы данных")

    create_book(
        session,
        "Python для начинающих",
        "Книга для изучения базового синтаксиса Python.",
        1200,
        "",
        programming.id
    )

    create_book(
        session,
        "Автоматизация на Python",
        "Книга о создании простых скриптов и автоматизации задач.",
        1500,
        "",
        programming.id
    )

    create_book(
        session,
        "PostgreSQL на практике",
        "Книга о проектировании и использовании PostgreSQL.",
        1800,
        "",
        databases.id
    )

    create_book(
        session,
        "SQLAlchemy и Python",
        "Книга о работе с базами данных через ORM SQLAlchemy.",
        2100,
        "",
        databases.id
    )

    print("База данных создана и заполнена тестовыми данными.")
finally:
    session.close()