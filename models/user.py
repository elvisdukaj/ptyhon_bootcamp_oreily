from datetime import datetime

from models.base import Base
from sqlalchemy import Integer, TIMESTAMP, String
from sqlalchemy.orm import mapped_column


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    created_at = mapped_column(TIMESTAMP, default=datetime.utcnow)
    username = mapped_column(String(25), unique=True, nullable=False)
    short_description = mapped_column(String(150), nullable=True)
    long_bio = mapped_column(String, nullable=True)
