from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db/{POSTGRES_DB}"


SECRET_KEY = "45e76c0a8ca3d8e14ea260c0d9f05da92d1d6c961f78b5db567ebebd3a712510"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

LOGGER = {
    "path": str(Path(BASE_DIR / 'custom_logging/access.log')),
    "level": "info",
    "rotation": "20 days",
    "retention": "1 months"
}
