from typing import List, Any

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.books import Books as schemas_User

router = APIRouter()


@router.post("/get_books", response_model=List[schemas_User])
def read_users(
        db: Session = Depends(deps.get_db)
) -> Any:
    books = crud.crud_books.book.get_all(db)
