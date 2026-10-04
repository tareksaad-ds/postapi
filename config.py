from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "" 
    secret_key: SecretStr = SecretStr("change-this-secret-key")
    algorithm: str = "HS256"
    access_token_expire_mintues: int = 30

    max_upload_size_bytes: int = 5 * 1024 * 1024  # 5 MB
    posts_per_page: int = 10
    reset_token_expire_minutes: int = 60

    mail_server: str = "smtp.example.com"
    mail_port: int = 2525
    mail_username: str = ""
    mail_password: SecretStr = SecretStr("")
    mail_use_tls: bool = True
    mail_from: str = "noreply@fastapiblog.com"

    frontend_url: str = "http://localhost:8000"

settings = Settings()
