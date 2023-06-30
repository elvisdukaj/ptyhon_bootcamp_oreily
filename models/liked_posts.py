from datetime import datetime

from models.base import Base
from sqlalchemy import Integer, TIMESTAMP, ForeignKey, Index
from sqlalchemy.orm import mapped_column


class LikedPosts(Base):
    __tablename__ = "liked_posts"

    id = mapped_column(Integer, primary_key=True)
    created_at = mapped_column(TIMESTAMP, default=datetime.utcnow)
    user_id = mapped_column(ForeignKey("user.id"), nullable=False, unique=True, index=True)
    post_id = mapped_column(Integer, nullable=False, unique=True)

# Index("liked_posts_user_id_idx",)
