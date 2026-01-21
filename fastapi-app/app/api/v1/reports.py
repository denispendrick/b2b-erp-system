from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from uuid import UUID
from app.database import get_db
from app.core.auth import get_current_active_user
from app.core.dependencies import get_organization_id
from app.models.product import Product
from app.models.inventory import InventoryLevel
from app.models.order import SalesOrder, PurchaseOrder
from app.models.invoice import Invoice
from app.models.user import User

router = APIRouter()


@router.get("/inventory/stock-valuation")
async def stock_valuation_report(
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get stock valuation report"""
    # Calculate total stock value
    stock_data = db.query(
        func.sum(InventoryLevel.quantity_on_hand * Product.cost_price).label("total_value"),
        func.count(Product.id).label("product_count")
    ).join(Product).filter(
        InventoryLevel.organization_id == organization_id
    ).first()

    return {
        "total_value": float(stock_data.total_value or 0),
        "product_count": stock_data.product_count or 0
    }


@router.get("/sales/summary")
async def sales_summary_report(
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get sales summary report"""
    sales_data = db.query(
        func.count(SalesOrder.id).label("order_count"),
        func.sum(SalesOrder.total_amount).label("total_sales")
    ).filter(
        SalesOrder.organization_id == organization_id,
        SalesOrder.status != "CANCELLED"
    ).first()

    return {
        "order_count": sales_data.order_count or 0,
        "total_sales": float(sales_data.total_sales or 0)
    }


@router.get("/purchases/summary")
async def purchase_summary_report(
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get purchase summary report"""
    purchase_data = db.query(
        func.count(PurchaseOrder.id).label("order_count"),
        func.sum(PurchaseOrder.total_amount).label("total_purchases")
    ).filter(
        PurchaseOrder.organization_id == organization_id,
        PurchaseOrder.status != "CANCELLED"
    ).first()

    return {
        "order_count": purchase_data.order_count or 0,
        "total_purchases": float(purchase_data.total_purchases or 0)
    }


@router.get("/accounts-receivable")
async def accounts_receivable_report(
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get accounts receivable aging report"""
    invoices_data = db.query(
        func.count(Invoice.id).label("invoice_count"),
        func.sum(Invoice.total_amount).label("total_invoiced"),
        func.sum(Invoice.paid_amount).label("total_paid"),
        func.sum(Invoice.balance_due).label("total_outstanding")
    ).filter(
        Invoice.organization_id == organization_id,
        Invoice.status != "CANCELLED"
    ).first()

    return {
        "invoice_count": invoices_data.invoice_count or 0,
        "total_invoiced": float(invoices_data.total_invoiced or 0),
        "total_paid": float(invoices_data.total_paid or 0),
        "total_outstanding": float(invoices_data.total_outstanding or 0)
    }


@router.get("/dashboard/kpis")
async def dashboard_kpis(
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get key performance indicators for dashboard"""
    # Get sales data
    sales = db.query(
        func.sum(SalesOrder.total_amount)
    ).filter(
        SalesOrder.organization_id == organization_id,
        SalesOrder.status != "CANCELLED"
    ).scalar()

    # Get inventory value
    inventory_value = db.query(
        func.sum(InventoryLevel.quantity_on_hand * Product.cost_price)
    ).join(Product).filter(
        InventoryLevel.organization_id == organization_id
    ).scalar()

    # Get pending orders
    pending_orders = db.query(func.count(SalesOrder.id)).filter(
        SalesOrder.organization_id == organization_id,
        SalesOrder.status.in_(["DRAFT", "CONFIRMED"])
    ).scalar()

    # Get outstanding invoices
    outstanding_invoices = db.query(
        func.sum(Invoice.balance_due)
    ).filter(
        Invoice.organization_id == organization_id,
        Invoice.balance_due > 0
    ).scalar()

    return {
        "total_sales": float(sales or 0),
        "inventory_value": float(inventory_value or 0),
        "pending_orders": pending_orders or 0,
        "outstanding_invoices": float(outstanding_invoices or 0)
    }
