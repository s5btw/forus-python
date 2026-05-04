from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db import crud
from app.db.db import get_db
from app.schemas import BookCreate, BookResponse, BookUpdate

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def read_books(
    category_id: int | None = Query(default=None),
    db: Session = Depends(get_db)
):
    return crud.get_books(db, category_id)


@router.get("/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, book.category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")

    return crud.create_book(
        db,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    if book.category_id is not None:
        category = crud.get_category(db, book.category_id)

        if category is None:
            raise HTTPException(status_code=404, detail="Категория не найдена")

    updated_book = crud.update_book(
        db,
        book_id,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )

    if updated_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return updated_book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    is_deleted = crud.delete_book(db, book_id)

    if not is_deleted:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return {"message": "Книга удалена"}
