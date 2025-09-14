from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from repository import accounts as accounts_repo
from schemas import ShowAccount, CreateAccount, UpdateAccount

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.get("/", status_code=200, response_model=List[ShowAccount])
def all(db: Session = Depends(get_db)):
    return accounts_repo.get_all(db)



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowAccount)
def create(request: CreateAccount, db: Session = Depends(get_db)):
    return accounts_repo.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def destroy(id: int, db: Session = Depends(get_db)):
    accounts_repo.destroy(id, db)
    return {"detail": f"Account {id} deleted successfully"}

    


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=ShowAccount)
def update(id: int, request: UpdateAccount, db: Session = Depends(get_db)):
    return accounts_repo.update(id, request, db)


@router.get("/{id}", status_code=200, response_model=ShowAccount)
def show(id: int, db: Session = Depends(get_db)):
    return accounts_repo.show(id, db)
