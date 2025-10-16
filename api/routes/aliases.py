from fastapi import APIRouter, Depends, HTTPException,status
from sqlmodel import Session, select
from typing import List
from datetime import datetime, timezone
from databases.postgres_db import get_session
from models.alias import Alias
from models.address import Address

router = APIRouter(prefix="/aliases", tags=["Aliases"])


@router.get("/", response_model=List[Alias], description="Get all aliases")
def get_aliases(offset: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    aliases = session.exec(select(Alias).offset(offset).limit(limit)).all()
    return aliases


@router.get("/{alias_id}", response_model=Alias, description="Get an alias by ID")
def get_alias(alias_id: int, session: Session = Depends(get_session)):
    alias = session.get(Alias, alias_id)
    if not alias:
        raise HTTPException(status_code=404, detail="Alias not found")
    return alias


@router.post("/", response_model=Alias,status_code=status.HTTP_201_CREATED, description="Create a new alias")
def create_alias(alias: Alias, session: Session = Depends(get_session)):
    # Check if the address_id exists
    address = session.get(Address, alias.address_id)
    if not address:
        raise HTTPException(status_code=400, detail="Invalid address_id. Address not found.")
    
    alias.created_at = datetime.now(timezone.utc)
    alias.updated_at = datetime.now(timezone.utc)
    session.add(alias)
    session.commit()
    session.refresh(alias)
    return alias


@router.put("/{alias_id}", response_model=Alias, description="Update an alias")
def update_alias(alias_id: int, alias: Alias, session: Session = Depends(get_session)):
    current_alias = session.get(Alias, alias_id)
    if not current_alias:
        raise HTTPException(status_code=404, detail="Alias not found")
    
    alias_data = alias.model_dump(exclude_unset=True)
    for key, value in alias_data.items():
        setattr(current_alias, key, value)
    current_alias.updated_at = datetime.now(timezone.utc)
    
    session.add(current_alias)
    session.commit()
    session.refresh(current_alias)
    return current_alias


@router.delete("/{alias_id}", status_code=status.HTTP_204_NO_CONTENT, description="Delete an alias by ID")
def delete_alias(alias_id: int, session: Session = Depends(get_session)):
    alias = session.get(Alias, alias_id)
    if not alias:
        raise HTTPException(status_code=404, detail="Alias not found")
    session.delete(alias)
    session.commit()
    return {"deleted": True}
