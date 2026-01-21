from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.core.auth import get_current_active_user
from app.core.dependencies import get_organization_id
from app.models.inventory import InventoryLevel, StockMovement, StockAdjustment, Warehouse
from app.models.user import User

router = APIRouter()


@router.get("/stock-levels")
async def get_stock_levels(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get stock levels for all products"""
    stock_levels = db.query(InventoryLevel).filter(
        InventoryLevel.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return stock_levels


@router.get("/stock-movements")
async def get_stock_movements(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get stock movement history"""
    movements = db.query(StockMovement).filter(
        StockMovement.organization_id == organization_id
    ).order_by(StockMovement.movement_date.desc()).offset(skip).limit(limit).all()
    return movements


@router.get("/warehouses")
async def get_warehouses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get all warehouses"""
    warehouses = db.query(Warehouse).filter(
        Warehouse.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return warehouses
