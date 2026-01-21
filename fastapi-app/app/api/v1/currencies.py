from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.core.auth import get_current_active_user
from app.models.currency import Currency, ExchangeRate
from app.models.user import User

router = APIRouter()


@router.get("/")
async def list_currencies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """List all currencies"""
    currencies = db.query(Currency).filter(Currency.is_active == True).all()
    return currencies


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_currency(
    currency_data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new currency"""
    new_currency = Currency(**currency_data)
    db.add(new_currency)
    db.commit()
    db.refresh(new_currency)
    return new_currency


@router.get("/exchange-rates")
async def list_exchange_rates(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """List exchange rates"""
    rates = db.query(ExchangeRate).offset(skip).limit(limit).all()
    return rates


@router.post("/exchange-rates", status_code=status.HTTP_201_CREATED)
async def create_exchange_rate(
    rate_data: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new exchange rate"""
    new_rate = ExchangeRate(**rate_data)
    db.add(new_rate)
    db.commit()
    db.refresh(new_rate)
    return new_rate
