from sqlalchemy.orm import Session
from sql_app import models
from log.log_setting import logger


async def add_url(db: Session, url: str, url_shorter: str) -> bool:
    """Добавляем новую запись в таблицу"""
    try:
        db_url = models.URL(url=url, url_shorter=url_shorter)
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        return True
    except BaseException as err:
        logger.error(f"При добавлении записи в БД URL произошла ошибка:\n {err}")
        return False


async def search_url_and_url_shorter(db: Session, url: str, url_shorter: str):
    """Проверяем есть ли в таблице URL такой url и url_shorter"""
    try:
        if result := db.query(models.URL).filter(models.URL.url == url,
                                        models.URL.url_shorter == url_shorter).first():
            return result
        return False
    except BaseException as err:
        logger.error(f"При поиска записи в БД URL произошла ошибка:\n {err}")
        raise Exception("Произошла поиска URL!")


async def get_url_by_url_short(db: Session, url_shorter: str):
    """Получаем URL по url_shorter"""
    try:
        if result := db.query(models.URL).filter(models.URL.url_shorter == url_shorter).first():
            return result
        return False
    except BaseException as err:
        logger.error(f"Произошла ошибка поиска URL!:\n {err}")
        raise Exception("Произошла ошибка поиска URL!")


async def update_count_requests(db: Session, url_shorter: str):
    """Добавляем +1 к count_requests"""
    try:
        db.query(models.URL).filter(models.URL.url_shorter == url_shorter).\
            update({"count_requests": (models.URL.count_requests + 1)})
        db.commit()
    except BaseException as err:
        logger.error(f"Произошла ошибка обновления данный!:\n {err}")
        raise Exception("Произошла ошибка обновления данный!")