from fastapi import APIRouter

from app.api.api_v1.routers import books

api_router = APIRouter()

api_router.include_router(books.router, prefix="/books", tags=["books"])
