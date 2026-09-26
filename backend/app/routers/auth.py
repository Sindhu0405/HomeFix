from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..schemas import (
    RegisterRequest,
    LoginRequest,
    AuthResponse
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


# =========================
# REGISTER
# =========================

@router.post("/register", response_model=AuthResponse)
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):

    name = data.name.strip()

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Name is required."
        )

    if not data.password:
        raise HTTPException(
            status_code=400,
            detail="Password is required."
        )

    # Check if name already exists
    existing_user = (
        db.query(User)
        .filter(User.name == name)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="This name is already registered."
        )

    user = User(
        name=name,
        password=data.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return AuthResponse(
        success=True,
        message="Account created successfully.",
        user_id=user.id,
        name=user.name
    )


# =========================
# LOGIN
# =========================

@router.post("/login", response_model=AuthResponse)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    name = data.name.strip()

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Name is required."
        )

    user = (
        db.query(User)
        .filter(User.name == name)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Account not found. Please create an account first."
        )

    if user.password != data.password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password."
        )

    return AuthResponse(
        success=True,
        message="Login successful.",
        user_id=user.id,
        name=user.name
    )