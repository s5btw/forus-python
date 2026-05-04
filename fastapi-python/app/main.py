from fastapi import FastAPI

from app.api.books import router as books_router
from app.api.categories import router as categories_router

app = FastAPI(
    title="Books API",
    description="API для работы с книгами и категориями",
    version="1.0.0"
)

app.include_router(categories_router)
app.include_router(books_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
