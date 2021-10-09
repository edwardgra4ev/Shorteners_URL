from fastapi import Depends
from sqlalchemy.orm import Session
from schemes import schemes
from sql_app import sql_queries
from app.main_app import application as app
from app.main_app import get_db


@app.post("/create_short_url")
async def create(data: schemes.CreateShortURL,  db: Session = Depends(get_db)):
    result = await sql_queries.search_url_and_url_shorter(db=db, url=data.url, url_shorter=data.name)
    if result is False:
        if await sql_queries.add_url(db=db, url_shorter=data.name, url=data.url):
            return {"short_url": f'http://localhost:8000/{data.name}'}
        else:
            return {"error": f"Короткое имя: '{data.name}' уже занято"}
    else:
        return {"short_url": f'http://localhost:8000/{result.url_shorter}'}
