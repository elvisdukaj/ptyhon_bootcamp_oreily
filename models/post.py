# from datetime import datetime
#
# from models.base import Base
# from sqlalchemy import Column, Integer, String, TIMESTAMP,  UniqueConstraint, ForeignKeyConstraint, Index
#
#
# class Post(Base):
#     __tablename__ = "post"
#
#     __table_args__ = (UniqueConstraint("id", name="post_id_constraint"),
#                       ForeignKeyConstraint("user_id", "user.id")
#                       )
#
#     id = Column(Integer, primary_key=True)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)
#     user_id = Column(Integer, nullable=False)
#     text = Column(String)
#
#
# # Index("liked_posts_user_id_idx",)
#
