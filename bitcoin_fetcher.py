"""
Bitcoin price fetcher module.
Fetches current Bitcoin price from CoinGecko API.
"""

import requests
import logging
from typing import Dict, Optional
from datetime import datetime
from config import Config

logger = logging.getLogger(__name__)


class BitcoinFetcher:
    """Fetches Bitcoin price data from CoinGecko API."""

    def __init__(self):
        """Initialize Bitcoin fetcher."""
        self.api_url = Config.BITCOIN_API_URL
        self.currency = Config.BITCOIN_VS_CURRENCY.lower()
        self.timeout = 10

    def get_bitcoin_price(self) -> Optional[Dict]:
        """
        Fetch current Bitcoin price.

        Returns:
            Dict with price data including:
            - price: Current Bitcoin price
            - market_cap: Market capitalization
            - market_cap_rank: Market cap rank
            - high_24h: 24 hour high
            - low_24h: 24 hour low
            - price_change_24h: 24 hour price change
            - price_change_percentage_24h: 24 hour price change percentage
            - timestamp: Fetch timestamp
            Returns None if fetch fails
        """
        try:
            url = f"{self.api_url}/simple/price"
            params = {
                'ids': 'bitcoin',
                'vs_currencies': self.currency,
                'include_market_cap': 'true',
                'include_24hr_vol': 'true',
                'include_24hr_change': 'true',
                'include_last_updated_at': 'true'
            }

            response = requests.get(
                url,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()

            data = response.json()

            if 'bitcoin' not in data:
                logger.error("Bitcoin data not found in API response")
                return None

            bitcoin_data = data['bitcoin']

            return {
                'price': bitcoin_data.get(self.currency, 0),
                'market_cap': bitcoin_data.get(f'{self.currency}_market_cap', 0),
                'market_cap_rank': bitcoin_data.get('market_cap_rank', 0),
                'high_24h': bitcoin_data.get(f'{self.currency}_24h_high', 0),
                'low_24h': bitcoin_data.get(f'{self.currency}_24h_low', 0),
                'price_change_24h': bitcoin_data.get(
                    f'{self.currency}_24h_change', 0
                ),
                'price_change_percentage_24h': bitcoin_data.get(
                    f'{self.currency}_24h_change_percentage', 0
                ),
                'timestamp': datetime.now()
            }

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch Bitcoin price: {e}")
            return None
        except (KeyError, ValueError) as e:
            logger.error(f"Error parsing Bitcoin price data: {e}")
            return None

    def format_price_message(self, price_data: Dict) -> str:
        """
        Format price data into a readable message.

        Args:
            price_data: Dictionary with price information

        Returns:
            Formatted message string
        """
        if not price_data:
            return "❌ Не удалось получить цену Bitcoin"

        currency_symbol = '$' if self.currency == 'usd' else self.currency.upper()
        price = price_data['price']
        change_24h = price_data['price_change_24h']
        change_pct = price_data['price_change_percentage_24h']
        high_24h = price_data['high_24h']
        low_24h = price_data['low_24h']
        market_cap = price_data['market_cap']

        change_emoji = '📈' if change_24h >= 0 else '📉'
        change_sign = '+' if change_24h >= 0 else ''

        timestamp = price_data['timestamp'].strftime('%H:%M:%S')

        message = (
            f"💰 <b>Bitcoin Price Alert</b> {change_emoji}\n\n"
            f"<b>Цена Bitcoin:</b> {currency_symbol}{price:,.2f}\n"
            f"<b>Изменение за 24ч:</b> {change_sign}{change_24h:,.2f} "
            f"({change_sign}{change_pct:.2f}%)\n"
            f"<b>Максимум 24ч:</b> {currency_symbol}{high_24h:,.2f}\n"
            f"<b>Минимум 24ч:</b> {currency_symbol}{low_24h:,.2f}\n"
            f"<b>Market Cap:</b> {currency_symbol}{market_cap:,.0f}\n\n"
            f"<i>Обновлено: {timestamp}</i>"
        )

        return message
