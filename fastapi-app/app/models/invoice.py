from sqlalchemy import Column, String, Numeric, DateTime, Text, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    invoice_number = Column(String(50), unique=True, nullable=False)
    sales_order_id = Column(UUID(as_uuid=True), ForeignKey("sales_orders.id"))
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"))
    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(String(50), default="DRAFT")  # DRAFT, SENT, PAID, PARTIAL, OVERDUE, CANCELLED
    currency = Column(String(3), default="USD")
    exchange_rate = Column(Numeric(12, 6), default=1.0)
    subtotal = Column(Numeric(15, 2))
    tax_amount = Column(Numeric(15, 2))
    total_amount = Column(Numeric(15, 2))
    paid_amount = Column(Numeric(15, 2), default=0)
    balance_due = Column(Numeric(15, 2))
    payment_terms = Column(String(100))
    notes = Column(Text)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="invoice")


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id", ondelete="CASCADE"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    description = Column(Text)
    quantity = Column(Numeric(15, 4), nullable=False)
    unit_price = Column(Numeric(15, 4), nullable=False)
    discount_percent = Column(Numeric(5, 2), default=0)
    tax_rate = Column(Numeric(5, 2))
    line_total = Column(Numeric(15, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    invoice = relationship("Invoice", back_populates="items")


class Payment(Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"))
    payment_number = Column(String(50), unique=True, nullable=False)
    payment_date = Column(Date, nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    payment_method = Column(String(50))  # CASH, CREDIT_CARD, BANK_TRANSFER, CHECK
    reference_number = Column(String(100))
    notes = Column(Text)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    invoice = relationship("Invoice", back_populates="payments")


class CreditNote(Base):
    __tablename__ = "credit_notes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    credit_note_number = Column(String(50), unique=True, nullable=False)
    invoice_id = Column(UUID(as_uuid=True), ForeignKey("invoices.id"))
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"))
    credit_date = Column(Date, nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    reason = Column(String(255))
    notes = Column(Text)
    status = Column(String(50), default="DRAFT")  # DRAFT, APPROVED, APPLIED
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
