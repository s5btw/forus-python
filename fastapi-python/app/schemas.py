from pydantic import BaseModel


class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class BookBase(BaseModel):
    title: str
    description: str
    price: float
    url: str | None = None
    category_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    url: str | None = None
    category_id: int | None = None


class BookResponse(BookBase):
    id: int

    model_config = {
        "from_attributes": True
    }
