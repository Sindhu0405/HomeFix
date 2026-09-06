from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Appliance
from ..schemas import ApplianceCreate, ApplianceOut

router = APIRouter(prefix="/api/appliances", tags=["Appliances"])


@router.post("", response_model=ApplianceOut, status_code=201)
def create_appliance(payload: ApplianceCreate, db: Session = Depends(get_db)):
    appliance = Appliance(**payload.model_dump())
    db.add(appliance)
    db.commit()
    db.refresh(appliance)
    return appliance


@router.get("", response_model=list[ApplianceOut])
def list_appliances(db: Session = Depends(get_db)):
    return db.query(Appliance).order_by(Appliance.id.desc()).all()


@router.get("/{appliance_id}", response_model=ApplianceOut)
def get_appliance(appliance_id: int, db: Session = Depends(get_db)):
    appliance = db.get(Appliance, appliance_id)
    if not appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")
    return appliance


@router.delete("/{appliance_id}", status_code=204)
def delete_appliance(appliance_id: int, db: Session = Depends(get_db)):
    appliance = db.get(Appliance, appliance_id)
    if not appliance:
        raise HTTPException(status_code=404, detail="Appliance not found")
    db.delete(appliance)
    db.commit()
