from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.division import Division, DivisionCreate, DivisionUpdate
from app.services import division_service

router = APIRouter()

@router.post("/divisions/", response_model=Division)
def create_division(division: DivisionCreate, db: Session = Depends(get_db)):
    return division_service.create_division(db=db, division=division)

@router.get("/divisions/", response_model=List[Division])
def read_divisions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return division_service.get_divisions(db, skip=skip, limit=limit)

@router.get("/divisions/{division_id}", response_model=Division)
def read_division(division_id: int, db: Session = Depends(get_db)):
    db_division = division_service.get_division(db, division_id=division_id)
    if db_division is None:
        raise HTTPException(status_code=404, detail="Division not found")
    return db_division

@router.put("/divisions/{division_id}", response_model=Division)
def update_division(division_id: int, division: DivisionUpdate, db: Session = Depends(get_db)):
    db_division = division_service.update_division(db, division_id=division_id, division=division)
    if db_division is None:
        raise HTTPException(status_code=404, detail="Division not found")
    return db_division

@router.delete("/divisions/{division_id}", response_model=Division)
def delete_division(division_id: int, db: Session = Depends(get_db)):
    db_division = division_service.delete_division(db, division_id=division_id)
    if db_division is None:
        raise HTTPException(status_code=404, detail="Division not found")
    return db_division
