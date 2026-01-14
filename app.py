"""
Bitcoin Price Telegram Alert Application.
Monitors Bitcoin price and sends notifications 4 times per day via Telegram.
"""

import logging
import schedule
import time
from datetime import datetime
from typing import List
from config import Config
from bitcoin_fetcher import BitcoinFetcher
from telegram_handler import TelegramHandler

# Configure logging
logging.basicConfig(
    level=Config.LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BitcoinPriceMonitor:
    """Main application class for monitoring Bitcoin price."""

    def __init__(self):
        """Initialize the Bitcoin price monitor."""
        self.bitcoin_fetcher = BitcoinFetcher()
        self.telegram_handler = TelegramHandler()
        self.notification_times: List[str] = Config.NOTIFICATION_TIMES
        self.timezone = Config.TIMEZONE

        logger.info("Bitcoin Price Monitor initialized")
        logger.info(f"Notification times: {', '.join(self.notification_times)}")
        logger.info(f"Timezone: {self.timezone}")

    def get_bitcoin_price_and_notify(self) -> None:
        """
        Fetch Bitcoin price and send notification.
        This is the main job that runs on schedule.
        """
        logger.info("Starting Bitcoin price fetch and notification...")

        try:
            # Fetch Bitcoin price
            price_data = self.bitcoin_fetcher.get_bitcoin_price()

            if price_data is None:
                error_message = (
                    "❌ <b>Bitcoin Price Alert</b>\n\n"
                    "Не удалось получить текущую цену Bitcoin.\n"
                    "Пожалуйста, проверьте интернет соединение."
                )
                self.telegram_handler.send_message(error_message)
                logger.error("Failed to fetch Bitcoin price")
                return

            # Format and send message
            message = self.bitcoin_fetcher.format_price_message(price_data)
            success = self.telegram_handler.send_message(message)

            if success:
                logger.info(
                    f"Bitcoin price notification sent successfully. "
                    f"Current price: ${price_data['price']:,.2f}"
                )
            else:
                logger.error("Failed to send notification")

        except Exception as e:
            logger.error(f"Unexpected error in notification job: {e}")
            try:
                error_msg = f"⚠️ Error: {str(e)}"
                self.telegram_handler.send_message(error_msg)
            except Exception as send_error:
                logger.error(f"Failed to send error notification: {send_error}")

    def schedule_notifications(self) -> None:
        """Schedule notifications for specified times."""
        for time_str in self.notification_times:
            time_str = time_str.strip()
            schedule.every().day.at(time_str).do(
                self.get_bitcoin_price_and_notify
            )
            logger.info(f"Scheduled notification at {time_str}")

    def run(self) -> None:
        """Run the scheduler in infinite loop."""
        logger.info("=" * 60)
        logger.info("Bitcoin Price Monitor started")
        logger.info("=" * 60)

        # Test Telegram connection
        if not self.telegram_handler.test_connection():
            logger.error(
                "Failed to connect to Telegram. "
                "Please check your bot token and chat ID."
            )
            raise RuntimeError("Telegram connection failed")

        logger.info("Telegram connection successful")

        # Send welcome notification
        welcome_msg = (
            "🚀 <b>Bitcoin Price Monitor Started</b>\n\n"
            "Приложение запущено и готово к работе.\n"
            "Вы будете получать уведомления о цене Bitcoin "
            "в следующее время:\n"
        )
        for time_str in self.notification_times:
            welcome_msg += f"⏰ {time_str}\n"
        welcome_msg += (
            f"\n🕐 Часовой пояс: {self.timezone}\n"
            f"💱 Валюта: {Config.BITCOIN_VS_CURRENCY.upper()}"
        )

        self.telegram_handler.send_message(welcome_msg)

        # Schedule all notifications
        self.schedule_notifications()

        # Main loop
        logger.info("Entering main scheduler loop...")
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            logger.info("Scheduler interrupted by user")
            shutdown_msg = (
                "🛑 <b>Bitcoin Price Monitor Stopped</b>\n\n"
                "Приложение было остановлено."
            )
            self.telegram_handler.send_message(shutdown_msg)
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {e}")
            error_msg = f"💥 Critical error: {str(e)}"
            self.telegram_handler.send_message(error_msg)
            raise


def main():
    """Entry point for the application."""
    try:
        # Validate configuration
        Config.validate()

        # Create and run monitor
        monitor = BitcoinPriceMonitor()
        monitor.run()

    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        print(f"❌ Configuration Error: {e}")
        print("Please check your .env file and set required variables:")
        print("  - TELEGRAM_BOT_TOKEN")
        print("  - TELEGRAM_CHAT_ID")
        exit(1)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"❌ Fatal Error: {e}")
        exit(1)


if __name__ == '__main__':
    main()
