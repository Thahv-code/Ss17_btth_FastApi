from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from app.models.association import package_truck_table


class Truck(Base):
    __tablename__ = "trucks"

    id = Column(Integer, primary_key=True, index=True)
    license_plate = Column(String(20), nullable=False)

    packages = relationship(
        "Package", secondary=package_truck_table, back_populates="trucks"
    )
