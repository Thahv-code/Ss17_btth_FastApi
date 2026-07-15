from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from app.models.association import package_truck_table


class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    package_code = Column(String(50), unique=True, nullable=False)
    weight = Column(Float, nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)

    warehouse = relationship("Warehouse", back_populates="packages")

    waybill = relationship("Waybill", back_populates="package", uselist=False)
    trucks = relationship(
        "Truck", secondary=package_truck_table, back_populates="packages"
    )
