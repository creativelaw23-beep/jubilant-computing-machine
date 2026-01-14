#!/usr/bin/env python3
"""
Setup script for Bitcoin Price Telegram Alert Application.
Helps with initial configuration and testing.
"""

import os
import sys
from pathlib import Path

from config import Config
from bitcoin_fetcher import BitcoinFetcher
from telegram_handler import TelegramHandler


def print_header(text: str) -> None:
    """Print formatted header."""
    print(f"\n{'=' * 60}")
    print(f"{text:^60}")
    print(f"{'=' * 60}\n")


def print_section(text: str) -> None:
    """Print formatted section."""
    print(f"\n📌 {text}")
    print("-" * 60)


def setup_env_file() -> bool:
    """Create .env file from .env.example if it doesn't exist."""
    env_path = Path('.env')
    env_example_path = Path('.env.example')

    if env_path.exists():
        print_section("✅ .env file already exists")
        return True

    if not env_example_path.exists():
        print_section("❌ .env.example file not found")
        return False

    print_section("Creating .env file from .env.example")
    try:
        with open(env_example_path, 'r') as f:
            content = f.read()
        with open(env_path, 'w') as f:
            f.write(content)
        print("✅ .env file created successfully")
        print(f"📍 Location: {env_path.absolute()}")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False


def validate_configuration() -> bool:
    """Validate the configuration."""
    print_section("Validating Configuration")
    try:
        Config.validate()
        print("✅ Configuration is valid")
        print(f"   - Bot Token: {'*' * 20}...{Config.TELEGRAM_BOT_TOKEN[-4:]}")
        print(f"   - Chat ID: {Config.TELEGRAM_CHAT_ID}")
        print(f"   - Notification Times: {', '.join(Config.NOTIFICATION_TIMES)}")
        print(f"   - Timezone: {Config.TIMEZONE}")
        print(f"   - Currency: {Config.BITCOIN_VS_CURRENCY.upper()}")
        return True
    except ValueError as e:
        print(f"❌ Configuration validation failed: {e}")
        print("\n📝 Please set the following variables in .env:")
        print("   - TELEGRAM_BOT_TOKEN")
        print("   - TELEGRAM_CHAT_ID")
        return False


def test_telegram_connection() -> bool:
    """Test Telegram connection."""
    print_section("Testing Telegram Connection")
    try:
        handler = TelegramHandler()
        if handler.test_connection():
            print("✅ Telegram connection successful")
            return True
        else:
            print("❌ Telegram connection failed")
            return False
    except Exception as e:
        print(f"❌ Error testing Telegram: {e}")
        return False


def test_bitcoin_api() -> bool:
    """Test Bitcoin API."""
    print_section("Testing Bitcoin API")
    try:
        fetcher = BitcoinFetcher()
        price_data = fetcher.get_bitcoin_price()
        if price_data:
            print("✅ Bitcoin API connection successful")
            print(f"   - Current Price: ${price_data['price']:,.2f}")
            print(f"   - 24h Change: {price_data['price_change_percentage_24h']:+.2f}%")
            return True
        else:
            print("❌ Failed to fetch Bitcoin price")
            return False
    except Exception as e:
        print(f"❌ Error testing Bitcoin API: {e}")
        return False


def send_test_notification() -> bool:
    """Send test notification to Telegram."""
    print_section("Sending Test Notification")
    try:
        handler = TelegramHandler()
        if handler.send_test_notification():
            print("✅ Test notification sent successfully")
            print("   Check your Telegram chat for the message")
            return True
        else:
            print("❌ Failed to send test notification")
            return False
    except Exception as e:
        print(f"❌ Error sending test notification: {e}")
        return False


def main():
    """Run setup process."""
    print_header("Bitcoin Price Telegram Alert - Setup")

    steps = [
        ("Creating .env file", setup_env_file),
        ("Validating Configuration", validate_configuration),
        ("Testing Telegram Connection", test_telegram_connection),
        ("Testing Bitcoin API", test_bitcoin_api),
        ("Sending Test Notification", send_test_notification),
    ]

    results = {}
    for step_name, step_func in steps:
        try:
            results[step_name] = step_func()
        except Exception as e:
            print(f"❌ Unexpected error in {step_name}: {e}")
            results[step_name] = False

    # Summary
    print_header("Setup Summary")
    for step_name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {step_name}")

    all_passed = all(results.values())

    if all_passed:
        print("\n" + "=" * 60)
        print("🎉 Setup completed successfully!")
        print("=" * 60)
        print("\nYou can now run the application:")
        print("   python app.py")
        print("\nThe application will send Bitcoin price notifications at:")
        for time_str in Config.NOTIFICATION_TIMES:
            print(f"   ⏰ {time_str}")
        return 0
    else:
        print("\n" + "=" * 60)
        print("⚠️  Setup completed with some warnings")
        print("=" * 60)
        print("\nPlease fix the failed steps and try again.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
