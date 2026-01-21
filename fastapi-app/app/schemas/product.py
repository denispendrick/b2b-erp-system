from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from typing import Optional, Dict, Any


class ProductCategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryResponse(ProductCategoryBase):
    id: str
    organization_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    category_id: Optional[str] = None
    unit_of_measure: Optional[str] = None
    unit_price: Optional[Decimal] = None
    cost_price: Optional[Decimal] = None
    reorder_point: int = 0
    reorder_quantity: int = 0
    is_active: bool = True
    barcode: Optional[str] = None
    tax_rate: Optional[Decimal] = None
    attributes: Dict[str, Any] = {}


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[str] = None
    unit_of_measure: Optional[str] = None
    unit_price: Optional[Decimal] = None
    cost_price: Optional[Decimal] = None
    reorder_point: Optional[int] = None
    reorder_quantity: Optional[int] = None
    is_active: Optional[bool] = None
    barcode: Optional[str] = None
    tax_rate: Optional[Decimal] = None
    attributes: Optional[Dict[str, Any]] = None


class ProductResponse(ProductBase):
    id: str
    organization_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
