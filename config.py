"""
Configuration module for Bitcoin Price Telegram Alert Application.
Loads settings from environment variables.
"""

import os
from dotenv import load_dotenv
import pytz

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration."""

    # Telegram Configuration
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '')

    # Notification Schedule (4 times per day)
    # Format: HH:MM,HH:MM,HH:MM,HH:MM
    NOTIFICATION_TIMES = os.getenv(
        'NOTIFICATION_TIMES',
        '06:00,12:00,18:00,23:00'
    ).split(',')

    # Timezone for scheduling
    TIMEZONE = pytz.timezone(os.getenv('TIMEZONE', 'UTC'))

    # Bitcoin API Configuration
    BITCOIN_API_URL = os.getenv(
        'BITCOIN_API_URL',
        'https://api.coingecko.com/api/v3'
    )
    BITCOIN_VS_CURRENCY = os.getenv('BITCOIN_VS_CURRENCY', 'usd')

    # Application Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    APP_ENV = os.getenv('APP_ENV', 'production')

    # Validation
    @staticmethod
    def validate():
        """Validate required configuration."""
        if not Config.TELEGRAM_BOT_TOKEN:
            raise ValueError('TELEGRAM_BOT_TOKEN is required')
        if not Config.TELEGRAM_CHAT_ID:
            raise ValueError('TELEGRAM_CHAT_ID is required')
        return True


if __name__ == '__main__':
    Config.validate()
    print("Configuration loaded successfully!")
