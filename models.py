from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
import os

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise EnvironmentError("DATABASE_URL environment variable is not set. Please configure it to proceed.")
else:
    print("Database URL is set and ready to use.")

Base = declarative_base()


# Enum for book genres
class Genre(PyEnum):
    Adventure = "Adventure"
    Classic = "Classic"
    Crime = "Crime"
    Drama = "Drama"
    Fantasy = "Fantasy"
    Historical_Fiction = "Historical Fiction"
    Horror = "Horror"
    Literary_Fiction = "Literary Fiction"
    Mystery = "Mystery"
    History = "History"
    Science_Fiction = "Science Fiction"
    Thriller = "Thriller"
    Western = "Western"
    Dystopian = "Dystopian"
    Magical_Realism = "Magical Realism"
    Satire = "Satire"
    Biography = "Biography"
    Autobiography = "Autobiography"
    Self_Help = "Self-Help"
    Poetry = "Poetry"


class Role(PyEnum):
    USER = "user"
    ADMIN = "admin"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    interested_genre = Column(Enum(Genre), nullable=False)
    role = Column(Enum(Role), default=Role.USER, nullable=False)


class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    genre = Column(Enum(Genre), nullable=False)
    year_published = Column(Integer)
    summary = Column(String,nullable=True)


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, nullable=False)
    review_text = Column(String, nullable=True)
    rating = Column(Integer, nullable=False)

    book = relationship("Book", back_populates="reviews")

    @validates('rating')
    def validate_rating(self, key, value):
        value = int(value)
        # Check if rating is an integer
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail="Rating must be an integer")
        
        # Check if rating is between 1 and 5
        if value < 1 or value > 5:
            raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
        
        return value


Book.reviews = relationship("Review", back_populates="book")

# Async Database setup
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)