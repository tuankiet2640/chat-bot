from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.department import Department, DepartmentCreate, DepartmentUpdate
from app.services import department_service

router = APIRouter()

@router.post("/departments", response_model=Department)
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return department_service.create_department(db=db, department=department)

@router.get("/departments", response_model=List[Department])
def read_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = department_service.get_departments(db, skip=skip, limit=limit)
    return departments

@router.get("/departments/{department_id}", response_model=Department)
def read_department(department_id: int, db: Session = Depends(get_db)):
    db_department = department_service.get_department(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@router.put("/departments/{department_id}", response_model=Department)
def update_department(department_id: int, department: DepartmentUpdate, db: Session = Depends(get_db)):
    db_department = department_service.update_department(db, department_id=department_id, department=department)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@router.delete("/departments/{department_id}", response_model=Department)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    db_department = department_service.delete_department(db, department_id=department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department
