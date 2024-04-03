from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.auth import get_current_active_user
from app.models.user import User
from uuid import UUID


def get_organization_id(
    current_user: User = Depends(get_current_active_user)
) -> UUID:
    """Get the organization ID of the current user"""
    if not current_user.organization_id:
        raise HTTPException(status_code=400, detail="User has no organization")
    return current_user.organization_id
