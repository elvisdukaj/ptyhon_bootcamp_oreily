from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(
        title="The username",
        description="This is the username of the user",
        default=None
    )

    liked_posts: list[int] = Field(
        description="Array of liked posts",
    )


class FullUserProfile(User):
    short_bio: str
    long_bio: str


class CreateUserResponse(BaseModel):
    user_id: int


class UserListResponse(BaseModel):
    users: list[FullUserProfile]
    total_users: int
