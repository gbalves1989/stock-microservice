from pydantic.v1 import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    pass
    #API_VERSION: str = os.getenv("API_USER_VERSION")
    #API_URL = os.getenv("API_USER_URL")
    #API_PORT = int(os.getenv("API_USER_PORT"))


settings: Settings = Settings() 
