import random
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Worker(Base):
    __tablename__ = "worker"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    contact_info = Column(Text)
    role = Column(String(50))
    
    def generate_data(self, first_names: dict, last_names: dict):
        self.name = f"{random.choice(first_names).capitalize()} {random.choice(last_names).capitalize()}"
        phone = f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
        self.contact_info = f"{phone} Living at {random.randint(100, 999)} {random.choice(last_names).capitalize()} Street"
        role_choices = ["Collections Specialist", "Collections Supervisor"]
        # We want to give a 20% chance of being a supervisor
        if random.randint(1, 100) <= 20:
            self.role = role_choices[1]
        else:
            self.role = role_choices[0]
