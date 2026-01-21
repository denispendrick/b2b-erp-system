from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.core.auth import get_current_active_user
from app.core.dependencies import get_organization_id
from app.models.vendor import Vendor, VendorContact, VendorPriceList
from app.models.user import User

router = APIRouter()


@router.get("/")
async def list_vendors(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """List all vendors"""
    vendors = db.query(Vendor).filter(
        Vendor.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return vendors


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_vendor(
    vendor_data: dict,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new vendor"""
    new_vendor = Vendor(
        organization_id=organization_id,
        **vendor_data
    )
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    return new_vendor


@router.get("/{vendor_id}")
async def get_vendor(
    vendor_id: UUID,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get a specific vendor"""
    vendor = db.query(Vendor).filter(
        Vendor.id == vendor_id,
        Vendor.organization_id == organization_id
    ).first()

    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found"
        )

    return vendor


@router.put("/{vendor_id}")
async def update_vendor(
    vendor_id: UUID,
    vendor_data: dict,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Update a vendor"""
    vendor = db.query(Vendor).filter(
        Vendor.id == vendor_id,
        Vendor.organization_id == organization_id
    ).first()

    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found"
        )

    for field, value in vendor_data.items():
        setattr(vendor, field, value)

    db.commit()
    db.refresh(vendor)
    return vendor


@router.delete("/{vendor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_vendor(
    vendor_id: UUID,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Delete a vendor"""
    vendor = db.query(Vendor).filter(
        Vendor.id == vendor_id,
        Vendor.organization_id == organization_id
    ).first()

    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found"
        )

    db.delete(vendor)
    db.commit()
    return None
