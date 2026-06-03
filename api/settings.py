from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    # BUG: debug=True baked in, not read from env
    debug: bool = True
    db_url: str = 'sqlite:///./test.db'
