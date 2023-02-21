from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.books import Books, DescriptionBooks
from app.schemas.books import BooksCreate, BooksUpdate, DescriptionBooksCreate, DescriptionBooksUpdate


class CRUDBooks(CRUDBase[Books, BooksCreate, BooksUpdate]):

    def get_by_name(self, db: Session, *, name: str) -> Optional[Books]:
        return db.query(Books).filter(Books.name == name).first()

    def create(self, db: Session, *, obj_in: BooksCreate) -> Books:
        db_obj = Books(obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


class CRUDDescriptionBooks(CRUDBase[DescriptionBooks, DescriptionBooksCreate, DescriptionBooksUpdate]):

    def get_by_id(self, db: Session, *, id: str) -> Optional[DescriptionBooks]:
        return db.query(DescriptionBooks).filter(DescriptionBooks.id_book == id).first()

    def create(self, db: Session, *, obj_in: BooksCreate) -> DescriptionBooks:
        db_obj = DescriptionBooks(obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


description_book = CRUDDescriptionBooks(Books)
book = CRUDBooks(Books)
