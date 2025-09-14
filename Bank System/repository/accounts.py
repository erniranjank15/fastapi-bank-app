from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Accounts
from schemas import CreateAccount, UpdateAccount


def get_all(db: Session):
    return db.query(Accounts).all()
    


def create(request: CreateAccount, db: Session):
    new_account = Accounts(
        acc_holder_name=request.acc_holder_name,
        acc_type=request.acc_type,
        balance=request.balance,
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account


def destroy(id: int, db: Session):
    account_q = db.query(Accounts).filter(Accounts.acc_no == id)
    account = account_q.first()
    if not account:
        raise HTTPException(status_code=404, detail=f"Account with id {id} not found")
    account_q.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: UpdateAccount, db: Session):
    account_q = db.query(Accounts).filter(Accounts.acc_no == id)
    account = account_q.first()
    if not account:
        raise HTTPException(status_code=404, detail=f"Account with id {id} not found")

    update_data = request.dict(exclude_unset=True)
    if update_data:
        account_q.update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(account)

    return account


def show(id: int, db: Session):
    account = db.query(Accounts).filter(Accounts.acc_no == id).first()
    if not account:
        raise HTTPException(status_code=404, detail=f"Account with id {id} not found")
    return account
