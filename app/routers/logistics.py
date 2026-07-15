from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas import logistics as schemas
from app.services import logistics as services

router = APIRouter(prefix="/packages", tags=["Logistics Packages API"])


@router.post(
    "/",
    response_model=schemas.PackageDetailResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_package(data: schemas.PackageCreate, db: Session = Depends(get_db)):
    return services.create_new_package(db, data)


@router.get("/{package_id}", response_model=schemas.PackageDetailResponse)
def read_package(package_id: int, db: Session = Depends(get_db)):
    return services.get_package_details(db, package_id)
