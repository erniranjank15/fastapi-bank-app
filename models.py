from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base



class Accounts(Base):
    __tablename__ = "accounts"
    acc_no = Column(Integer, primary_key=True, index=True)
    acc_holder_name = Column(String, nullable=False)
    acc_type = Column(String, nullable=False)
    balance = Column(Float, default=0.0)