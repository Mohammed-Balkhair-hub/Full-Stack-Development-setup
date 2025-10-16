from fastapi import APIRouter, Depends, HTTPException,status
from sqlmodel import Session, select
from typing import List
from databases.postgres_db import get_session
from datetime import datetime, timezone
from models.user import User


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[User], description="Get all users")
def get_users(offset: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@router.get("/{user_id}", response_model=User, description="Get a user by ID")
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=User,status_code=status.HTTP_201_CREATED, description="Create a new user")
def create_user(user: User, session: Session = Depends(get_session)):
    user.created_at = datetime.now(timezone.utc)
    user.updated_at = datetime.now(timezone.utc)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.put("/{user_id}", response_model=User,description="Update the email of an existing user. Only the email field can be updated.")
def update_user(user_id: int, user: User, session: Session = Depends(get_session)):
    current_user = session.get(User, user_id)
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.model_dump(exclude_unset=True)
    if len(user_data) != 1 or "email" not in user_data:
        raise HTTPException(
            status_code=400, detail="Only the email field can be updated"
        )
    current_user.updated_at = datetime.now(timezone.utc)
    current_user.email = user_data["email"]
    session.add(current_user)
    session.commit()
    session.refresh(current_user)
    return current_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, description="Delete a user by ID")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(db_user)
    session.commit()
    return {"deleted": True}
