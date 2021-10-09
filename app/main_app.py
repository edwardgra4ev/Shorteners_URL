from fastapi import FastAPI
from sql_app.database import SessionLocal, engine
from sql_app import models


# Инициализация FastApi
application = FastAPI(
    title="Shorteners URL",
    description="Портал предназначен для сокращения URL по средством REST-API"
                "\nПроект написан на FastAPI с использованием sqlalchemy и SQL Lite",
    version="1.0.0",

)

models.Base.metadata.create_all(bind=engine)


# Соединение с бд
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()