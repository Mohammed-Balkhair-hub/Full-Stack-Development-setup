from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from typing import List
from typing import Optional


class Address(SQLModel, table=True):
    __tablename__ = "Address"
    
    address_id: int = Field(primary_key=True)
    building_number: int = Field(default=None)
    street: str = Field(default=None, max_length=100)
    district: str = Field(default=None, max_length=100)
    unit_number: int = Field(default=None)
    floor_number: int = Field(default=None)
    city: str = Field(nullable=False, max_length=100)
    region: str = Field(default=None, max_length=100)
    postal_code: str = Field(nullable=False, max_length=20)
    secondary_code: str = Field(default=None, max_length=20)
    short_code: str = Field(default=None, max_length=20)
    plus_code: str = Field(default=None, max_length=20)
    country: str = Field(nullable=False, max_length=100)
    latitude: float = Field(nullable=False)
    longitude: float = Field(nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # Relationships
    #many aliases to one address
    alias: List["Alias"] = Relationship(back_populates="address")

    #one residential to many addresses
    residential: Optional["Residential"] = Relationship(back_populates="addresses")

    #one business to many addresses
    business: Optional["Business"] = Relationship(back_populates="addresses")

    # one poi to one address
    poi: Optional["POI"] = Relationship(back_populates="address", sa_relationship_kwargs={"uselist": False})

    ##one validation to one address
    validation: Optional["Validation"] = Relationship(back_populates="address", sa_relationship_kwargs={"uselist": False})