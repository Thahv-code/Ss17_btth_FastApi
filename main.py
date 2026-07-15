from fastapi import FastAPI
from database import engine
from app.models import warehouse as model_warehouse
from app.models import package as model_package
from app.models import waybill as model_waybill
from app.models import truck as model_truck

from app.routers import logistics as router_logistics

model_warehouse.Base.metadata.create_all(bind=engine)
model_package.Base.metadata.create_all(bind=engine)
model_waybill.Base.metadata.create_all(bind=engine)
model_truck.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Logistics Management API")

app.include_router(router_logistics.router)


@app.get("/")
def root():
    return {
        "message": "Hệ thống Logistics đã thiết lập thành công mô hình dữ liệu chuẩn hóa!"
    }
