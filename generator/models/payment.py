
from sqlalchemy import Column, Integer, Date, DECIMAL, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase


from enums.payment_status_enum import PaymentStatusEnum

from models.case import Case

class Base(DeclarativeBase):
    pass

class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    case_id = Column(Integer, ForeignKey(Case.id), nullable=False)
    payment_date = Column(Date)
    payment_amount = Column(DECIMAL(precision=10, scale=2))
    
    # Define the choices for the payment_status field as an ENUM
    payment_status_enum = PaymentStatusEnum
    payment_status = Column(String, default=payment_status_enum.ON_TIME.value)
