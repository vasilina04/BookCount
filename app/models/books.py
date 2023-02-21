# Sereda Semen
# 2022, 06.10
import uuid

from sqlalchemy import Column, String, ForeignKey, Text

from app.db.base_class import Base


class Books(Base):
    id = Column(Text(length=36), nullable=False, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(20), nullable=False)


class DescriptionBooks(Base):
    id = Column(Text(length=36), nullable=False, primary_key=True, default=lambda: str(uuid.uuid4()))
    id_book = Column(Text(length=36), ForeignKey('books.id'), nullable=False)
    href = Column(String(), nullable=False)
    title = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    year = Column(String(), nullable=False)
    image_link = Column(String(), nullable=False)
    ISBN = Column(String(), nullable=False)
    number_page = Column(String(), nullable=False)
    genre = Column(String(), nullable=False)
    tags = Column(String(), nullable=False)
