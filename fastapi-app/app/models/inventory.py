from sqlalchemy import Column, String, Numeric, DateTime, Text, ForeignKey, Date, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Computed
import uuid
from app.database import Base


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    code = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    address = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    postal_code = Column(String(20))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    inventory_levels = relationship("InventoryLevel", back_populates="warehouse")


class InventoryLevel(Base):
    __tablename__ = "inventory_levels"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    warehouse_id = Column(UUID(as_uuid=True), ForeignKey("warehouses.id"))
    quantity_on_hand = Column(Numeric(15, 4), default=0)
    quantity_reserved = Column(Numeric(15, 4), default=0)
    quantity_available = Column(
        Numeric(15, 4),
        Computed("quantity_on_hand - quantity_reserved")
    )
    bin_location = Column(String(50))
    batch_number = Column(String(100))
    expiry_date = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="inventory_levels")
    warehouse = relationship("Warehouse", back_populates="inventory_levels")


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    warehouse_id = Column(UUID(as_uuid=True), ForeignKey("warehouses.id"))
    movement_type = Column(String(50), nullable=False)  # IN, OUT, TRANSFER, ADJUSTMENT
    quantity = Column(Numeric(15, 4), nullable=False)
    reference_type = Column(String(50))  # SALES_ORDER, PURCHASE_ORDER, ADJUSTMENT
    reference_id = Column(UUID(as_uuid=True))
    notes = Column(Text)
    movement_date = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class StockAdjustment(Base):
    __tablename__ = "stock_adjustments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    warehouse_id = Column(UUID(as_uuid=True), ForeignKey("warehouses.id"))
    adjustment_type = Column(String(50), nullable=False)  # INCREASE, DECREASE, COUNT
    quantity_before = Column(Numeric(15, 4), nullable=False)
    quantity_after = Column(Numeric(15, 4), nullable=False)
    quantity_change = Column(Numeric(15, 4), nullable=False)
    reason = Column(String(255))
    notes = Column(Text)
    adjustment_date = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
