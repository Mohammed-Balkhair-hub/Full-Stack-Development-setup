from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class User(SQLModel, table=True):
    __tablename__ = "Users"
    user_id: int = Field(primary_key=True)
    username: str = Field(max_length=56, unique=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = Field(
        default_factory=lambda: lambda: datetime.now(timezone.utc)
    )
