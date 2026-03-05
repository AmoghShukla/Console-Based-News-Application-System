from pydantic_settings import BaseSettings

class NewsAPIConfig(BaseSettings):
    API_Key: str
    Base_URL: str

    class Config:
        env_file = ".env"

    


newsapi = NewsAPIConfig()

API_KEY = newsapi.API_Key
BASE_URL = newsapi.Base_URL
Article_file = "data/Article.json"
Summary_file = "data/Summary.txt"