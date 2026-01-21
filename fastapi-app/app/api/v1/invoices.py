from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.core.auth import get_current_active_user
from app.core.dependencies import get_organization_id
from app.models.invoice import Invoice, InvoiceItem, Payment, CreditNote
from app.models.user import User

router = APIRouter()


@router.get("/")
async def list_invoices(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """List all invoices"""
    invoices = db.query(Invoice).filter(
        Invoice.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return invoices


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_invoice(
    invoice_data: dict,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new invoice"""
    new_invoice = Invoice(
        organization_id=organization_id,
        created_by=current_user.id,
        **invoice_data
    )
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice


@router.get("/{invoice_id}")
async def get_invoice(
    invoice_id: UUID,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get a specific invoice"""
    invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id,
        Invoice.organization_id == organization_id
    ).first()

    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )

    return invoice


@router.put("/{invoice_id}")
async def update_invoice(
    invoice_id: UUID,
    invoice_data: dict,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Update an invoice"""
    invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id,
        Invoice.organization_id == organization_id
    ).first()

    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )

    for field, value in invoice_data.items():
        setattr(invoice, field, value)

    db.commit()
    db.refresh(invoice)
    return invoice


@router.delete("/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_invoice(
    invoice_id: UUID,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Delete an invoice"""
    invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id,
        Invoice.organization_id == organization_id
    ).first()

    if not invoice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invoice not found"
        )

    db.delete(invoice)
    db.commit()
    return None


# Payments
@router.post("/payments", status_code=status.HTTP_201_CREATED)
async def create_payment(
    payment_data: dict,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Create a payment"""
    new_payment = Payment(
        organization_id=organization_id,
        created_by=current_user.id,
        **payment_data
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


@router.get("/payments")
async def list_payments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """List all payments"""
    payments = db.query(Payment).filter(
        Payment.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return payments
