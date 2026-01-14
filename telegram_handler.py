"""
Telegram bot handler module.
Manages Telegram bot operations and message sending.
"""

import logging
from typing import Optional
from telegram import Bot
from telegram.error import TelegramError
from config import Config

logger = logging.getLogger(__name__)


class TelegramHandler:
    """Handles Telegram bot operations."""

    def __init__(self):
        """Initialize Telegram handler."""
        try:
            self.bot = Bot(token=Config.TELEGRAM_BOT_TOKEN)
            self.chat_id = Config.TELEGRAM_CHAT_ID
            logger.info("Telegram handler initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Telegram handler: {e}")
            raise

    def send_message(self, message: str) -> bool:
        """
        Send message to Telegram chat.

        Args:
            message: Message text (supports HTML formatting)

        Returns:
            True if message sent successfully, False otherwise
        """
        try:
            self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode='HTML'
            )
            logger.info(f"Message sent to chat {self.chat_id}")
            return True
        except TelegramError as e:
            logger.error(f"Failed to send Telegram message: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error sending message: {e}")
            return False

    def test_connection(self) -> bool:
        """
        Test connection to Telegram API.

        Returns:
            True if connection successful, False otherwise
        """
        try:
            self.bot.get_me()
            logger.info("Telegram connection test successful")
            return True
        except TelegramError as e:
            logger.error(f"Telegram connection test failed: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error during connection test: {e}")
            return False

    def send_test_notification(self) -> bool:
        """
        Send a test notification to verify setup.

        Returns:
            True if test notification sent successfully
        """
        test_message = (
            "✅ <b>Bitcoin Price Monitor</b>\n\n"
            "Тестовое уведомление успешно отправлено!\n"
            "Приложение готово к работе. 🚀"
        )
        return self.send_message(test_message)
