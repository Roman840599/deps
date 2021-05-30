from pathlib import Path
from pydantic import BaseSettings, Field, SecretStr

config_dir = Path(__file__).resolve().parent


class DBConfig(BaseSettings):
    db: str = Field(..., env='DATABASE')
    user: str = Field(..., env='USER')
    password: SecretStr = Field(..., env='PASSWORD')
    host: str = Field(..., env='HOST')
    port: str = Field(..., env='PORT')

    class Config:
        env_file = Path(config_dir.parent / 'envs/.env.dev.db')
        env_file_encoding = 'utf-8'

    def get_connection_string(self):
        unsecured_password = self.password.get_secret_value()
        return f'postgresql://{self.user}:{unsecured_password}@{self.host}:{self.port}/{self.db}'


connection_configs = DBConfig()
