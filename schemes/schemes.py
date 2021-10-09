from pydantic import BaseModel, validator
import re
from log.log_setting import logger


class CreateShortURL(BaseModel):
    name: str
    url: str

    @validator('url')
    def url_verification(cls, url_string: str) -> str:
        if "https" in url_string:
            print(re.search("(?P<url>https?://[^\s]+)", url_string).group("url"))
            return url_string
        elif "http" in url_string:
            print(re.search("(?P<url>http?://[^\s]+)", url_string).group("url"))
            return url_string
        else:
            logger.info(f"\nURL указан некорректно!\nURL: {url_string}")
            raise ValueError("URL указан некорректно!")
