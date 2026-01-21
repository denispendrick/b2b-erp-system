from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from datetime import date
from decimal import Decimal
from app.database import get_db
from app.core.auth import get_current_active_user
from app.core.dependencies import get_organization_id
from app.models.order import SalesOrder, SalesOrderItem, PurchaseOrder, PurchaseOrderItem, Customer
from app.models.user import User

router = APIRouter()


# Sales Orders
@router.get("/sales")
async def list_sales_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """List all sales orders"""
    orders = db.query(SalesOrder).filter(
        SalesOrder.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return orders


@router.post("/sales", status_code=status.HTTP_201_CREATED)
async def create_sales_order(
    order_data: dict,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new sales order"""
    new_order = SalesOrder(
        organization_id=organization_id,
        created_by=current_user.id,
        **order_data
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/sales/{order_id}")
async def get_sales_order(
    order_id: UUID,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get a specific sales order"""
    order = db.query(SalesOrder).filter(
        SalesOrder.id == order_id,
        SalesOrder.organization_id == organization_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sales order not found"
        )

    return order


# Purchase Orders
@router.get("/purchases")
async def list_purchase_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """List all purchase orders"""
    orders = db.query(PurchaseOrder).filter(
        PurchaseOrder.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return orders


@router.post("/purchases", status_code=status.HTTP_201_CREATED)
async def create_purchase_order(
    order_data: dict,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new purchase order"""
    new_order = PurchaseOrder(
        organization_id=organization_id,
        created_by=current_user.id,
        **order_data
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@router.get("/purchases/{order_id}")
async def get_purchase_order(
    order_id: UUID,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get a specific purchase order"""
    order = db.query(PurchaseOrder).filter(
        PurchaseOrder.id == order_id,
        PurchaseOrder.organization_id == organization_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Purchase order not found"
        )

    return order


# Customers
@router.get("/customers")
async def list_customers(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """List all customers"""
    customers = db.query(Customer).filter(
        Customer.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return customers


@router.post("/customers", status_code=status.HTTP_201_CREATED)
async def create_customer(
    customer_data: dict,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new customer"""
    new_customer = Customer(
        organization_id=organization_id,
        **customer_data
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer
