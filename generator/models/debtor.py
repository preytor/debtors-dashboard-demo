import random
from enum import Enum
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class LegalStatusEnum(Enum):
    ACTIVE = "Active"
    IN_LITIGATION = "In litigation"
    CLOSED = "Closed"

class Debtor(Base):
    __tablename__ = "debtor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    contact_info = Column(Text)
    
    # Define the choices for the legal_status field as an ENUM
    legal_status_enum = LegalStatusEnum
    legal_status = Column(String, default=legal_status_enum.ACTIVE.value)

    def generate_data(self, first_names: list, last_names: list):
        self.name = f"{random.choice(first_names)} {random.choice(last_names)}"
        self.contact_info = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        self.legal_status = random.choice(self.legal_status_enum._member_names_)
        