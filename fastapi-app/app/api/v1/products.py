from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.core.auth import get_current_active_user
from app.core.dependencies import get_organization_id
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    ProductCategoryCreate,
    ProductCategoryResponse
)
from app.models.product import Product, ProductCategory
from app.models.user import User

router = APIRouter()


@router.get("/", response_model=List[ProductResponse])
async def list_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """List all products for the organization"""
    products = db.query(Product).filter(
        Product.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return products


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new product"""
    # Check if SKU already exists
    existing_product = db.query(Product).filter(Product.sku == product.sku).first()
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product with this SKU already exists"
        )

    new_product = Product(
        **product.model_dump(),
        organization_id=organization_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: UUID,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Get a specific product"""
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.organization_id == organization_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID,
    product_update: ProductUpdate,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Update a product"""
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.organization_id == organization_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    update_data = product_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: UUID,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Delete a product"""
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.organization_id == organization_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()
    return None


# Product Categories endpoints

@router.get("/categories/", response_model=List[ProductCategoryResponse])
async def list_product_categories(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """List all product categories"""
    categories = db.query(ProductCategory).filter(
        ProductCategory.organization_id == organization_id
    ).offset(skip).limit(limit).all()
    return categories


@router.post("/categories/", response_model=ProductCategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_product_category(
    category: ProductCategoryCreate,
    db: Session = Depends(get_db),
    organization_id: UUID = Depends(get_organization_id),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new product category"""
    new_category = ProductCategory(
        **category.model_dump(),
        organization_id=organization_id
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
