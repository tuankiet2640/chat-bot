from sqlalchemy.orm import Session
from app.models.division import Division
from app.schemas.division import DivisionCreate, DivisionUpdate

def get_division(db: Session, division_id: int):
    return db.query(Division).filter(Division.id == division_id).first()

def get_divisions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Division).offset(skip).limit(limit).all()

def create_division(db: Session, division: DivisionCreate):
    db_division = Division(name=division.name, department_id=division.department_id)
    db.add(db_division)
    db.commit()
    db.refresh(db_division)
    return db_division

def update_division(db: Session, division_id: int, division: DivisionUpdate):
    db_division = get_division(db, division_id=division_id)
    if db_division:
        update_data = division.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_division, field, value)
        db.commit()
        db.refresh(db_division)
    return db_division

def delete_division(db: Session, division_id: int):
    db_division = get_division(db, division_id)
    if db_division:
        db.delete(db_division)
        db.commit()
    return db_division
