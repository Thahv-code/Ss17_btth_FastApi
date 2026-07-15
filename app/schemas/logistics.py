from pydantic import BaseModel
from typing import List, Optional


class WaybillResponse(BaseModel):
    tracking_number: str
    shipping_status: str

    class Config:
        from_attributes = True


class TruckResponse(BaseModel):
    license_plate: str

    class Config:
        from_attributes = True


class PackageCreate(BaseModel):
    package_code: str
    weight: float
    warehouse_id: int


class PackageDetailResponse(BaseModel):
    id: int
    package_code: str
    weight: float
    warehouse_id: int

    waybill: Optional[WaybillResponse] = None
    trucks: List[TruckResponse] = []

    class Config:
        from_attributes = True
