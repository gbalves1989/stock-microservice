import os
from pydantic.v1 import BaseConfig
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseConfig):
    API_VERSION: str = os.getenv("API_CATEGORY_VERSION")
    API_URL = os.getenv("API_CATEGORY_URL")
    API_PORT = int(os.getenv("API_CATEGORY_PORT"))
    
    class Config:
        case_sensitive = True

settings: Settings = Settings() 
