"""
AgriSense AI - Configuration Settings
"""
import os
from typing import Optional

class Settings:
    # Application
    APP_NAME: str = "AgriSense AI"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./agrisense.db")
    
    # API Keys
    OPENWEATHER_API_KEY: Optional[str] = os.getenv("OPENWEATHER_API_KEY")
    WEATHERAPI_KEY: Optional[str] = os.getenv("WEATHERAPI_KEY")
    
    # External APIs
    ENAM_API_URL: str = os.getenv("ENAM_API_URL", "https://api.data.gov.in/resource/")
    AGMARKNET_API_URL: str = os.getenv("AGMARKNET_API_URL", "https://agmarknet.gov.in/")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:8000",
        "https://huggingface.co",
        "https://netlify.app",
        "https://vercel.app"
    ]
    
    # File Upload
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_FILE_TYPES: list = [".jpg", ".jpeg", ".png", ".pdf", ".csv"]
    
    # Notifications
    ENABLE_SMS: bool = os.getenv("ENABLE_SMS", "False").lower() == "true"
    ENABLE_EMAIL: bool = os.getenv("ENABLE_EMAIL", "False").lower() == "true"
    
    # Twilio (for SMS)
    TWILIO_ACCOUNT_SID: Optional[str] = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN: Optional[str] = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER: Optional[str] = os.getenv("TWILIO_PHONE_NUMBER")
    
    # Email
    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    EMAIL_USER: Optional[str] = os.getenv("EMAIL_USER")
    EMAIL_PASSWORD: Optional[str] = os.getenv("EMAIL_PASSWORD")

settings = Settings()
