from fastapi import APIRouter, Depends, HTTPException,status
from sqlmodel import Session, select
from typing import List
from datetime import datetime, timezone
from databases.postgres_db import get_session
from models.address import Address

router = APIRouter(prefix="/addresses", tags=["Addresses"])


@router.get("/", response_model=List[Address], description="Get all addresses")
def get_addresses(offset: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    addresses = session.exec(select(Address).offset(offset).limit(limit)).all()
    return addresses


@router.get("/{address_id}", response_model=Address, description="Get an address by ID")
def get_address(address_id: int, session: Session = Depends(get_session)):
    address = session.get(Address, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@router.post("/", response_model=Address,status_code=status.HTTP_201_CREATED, description="Create a new address")
def create_address(address: Address, session: Session = Depends(get_session)):
    address.created_at = datetime.now(timezone.utc)
    address.updated_at = datetime.now(timezone.utc)
    session.add(address)
    session.commit()
    session.refresh(address)
    return address


@router.put("/{address_id}", response_model=Address, description="Update an existing address")
def update_address(address_id: int, address: Address, session: Session = Depends(get_session)):
    current_address = session.get(Address, address_id)
    if not current_address:
        raise HTTPException(status_code=404, detail="Address not found")

    address_data = address.model_dump(exclude_unset=True)
    for key, value in address_data.items():
        setattr(current_address, key, value)
    current_address.updated_at = datetime.now(timezone.utc)

    session.add(current_address)
    session.commit()
    session.refresh(current_address)
    return current_address


@router.delete("/{address_id}",status_code=status.HTTP_204_NO_CONTENT, description="Delete an address by ID")
def delete_address(address_id: int, session: Session = Depends(get_session)):
    address = session.get(Address, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    session.delete(address)
    session.commit()
    return {"deleted": True}
