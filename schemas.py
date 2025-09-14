from pydantic import BaseModel
from typing import List, Optional






class CreateAccount(BaseModel):
    acc_holder_name: str
    acc_type: str
    balance: float = 0.0

    class Config:
        orm_mode = True





class UpdateAccount(BaseModel):
    acc_holder_name: Optional[str] = None
    acc_type: Optional[str] = None
    balance: Optional[float] = None

    class Config:
        orm_mode = True





class ShowAccount(BaseModel):
    acc_no: int
    acc_holder_name: str
    acc_type: str
    balance: float
 

    class Config:
        orm_mode = True