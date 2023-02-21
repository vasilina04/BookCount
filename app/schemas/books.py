from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class BooksBase(BaseModel):
    name: Optional[str] = None


class BooksCreate(BooksBase):
    name: str


class BooksUpdate(BooksBase):
    name: str


class BooksUpdateName(BooksBase):
    name: Optional[str] = None


class BooksInDBBase(BooksBase):
    id: UUID

    class Config:
        orm_mode = True


class Books(BooksInDBBase):
    pass


class DescriptionBooksBase(BaseModel):
    id_book: Optional[str] = None
    href: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    year: Optional[str] = None
    image_link: Optional[str] = None
    ISBN: Optional[str] = None
    number_page: Optional[str] = None
    genre: Optional[str] = None
    tags: Optional[str] = None


class DescriptionBooksCreate(DescriptionBooksBase):
    id_book: Optional[str]
    href: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    year: Optional[str] = None
    image_link: Optional[str] = None
    ISBN: Optional[str] = None
    number_page: Optional[str] = None
    genre: Optional[str] = None
    tags: Optional[str] = None


class DescriptionBooksUpdate(DescriptionBooksBase):
    href: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    year: Optional[str] = None
    image_link: Optional[str] = None
    ISBN: Optional[str] = None
    number_page: Optional[str] = None
    genre: Optional[str] = None
    tags: Optional[str] = None


class DescriptionBooksInDBBase(DescriptionBooksBase):
    id: UUID

    class Config:
        orm_mode = True


class DescriptionBooks(DescriptionBooksInDBBase):
    pass
