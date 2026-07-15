from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from app.models.package import Package
from app.models.warehouse import Warehouse
from app.schemas.logistics import PackageCreate


def create_new_package(db: Session, data: PackageCreate):
    warehouse = db.query(Warehouse).filter(Warehouse.id == data.warehouse_id).first()
    if not warehouse:
        raise HTTPException(status_code=404, detail="Nhà kho không tồn tại!")

    existing_package = (
        db.query(Package).filter(Package.package_code == data.package_code).first()
    )
    if existing_package:
        raise HTTPException(status_code=400, detail="Mã kiện hàng này đã tồn tại!")

    new_package = Package(
        package_code=data.package_code,
        weight=data.weight,
        warehouse_id=data.warehouse_id,
    )
    db.add(new_package)
    db.commit()
    db.refresh(new_package)
    return new_package


def get_package_details(db: Session, package_id: int):
    package = (
        db.query(Package)
        .options(joinedload(Package.waybill), joinedload(Package.trucks))
        .filter(Package.id == package_id)
        .first()
    )

    if not package:
        raise HTTPException(status_code=404, detail="Không tìm thấy kiện hàng!")

    return package
