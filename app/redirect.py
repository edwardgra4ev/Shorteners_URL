from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.responses import RedirectResponse
from sql_app import sql_queries
from app.main_app import application as app
from app.main_app import get_db


@app.get("/{short_url}")
async def redirect(short_url: str,  db: Session = Depends(get_db)):
    if result := await sql_queries.get_url_by_url_short(db=db, url_shorter=short_url):
        await sql_queries.update_count_requests(db=db, url_shorter=short_url)
        return RedirectResponse(str(result.url))
    else:
        return {"error": "Произошла ошибка при поиска URL"}