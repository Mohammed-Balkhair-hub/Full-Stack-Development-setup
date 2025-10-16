from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import Optional
from models.address import Address

class Alias(SQLModel, table=True):
    __tablename__ = "Aliases"

    alias_id: int = Field(primary_key=True)
    address_id: int = Field(nullable=False, foreign_key="Address.address_id")
    alias_name: str = Field(nullable=False, max_length=100)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    address: Optional[Address] = Relationship(back_populates="alias")