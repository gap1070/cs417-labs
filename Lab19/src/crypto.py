"""
Lab 19: API Requests and Caching

Fetch cryptocurrency prices from CoinGecko and cache them locally.
"""

import time
import requests


# CoinGecko API base URL
BASE_URL = "https://api.coingecko.com/api/v3"


def get_price(coin_id: str, api_key: str) -> float:
    response = requests.get(
        f"{BASE_URL}/simple/price", 
        params={
            "ids": coin_id, 
            "vs_currencies": "usd", 
            "x_cg_demo_api_key": api_key
        }
    )

    if response.status_code != 200:
        raise RuntimeError(response.status_code)
    
    data = response.json()
    return float(data[coin_id]["usd"])


def get_prices_batch(coin_ids: list, api_key: str) -> dict:
    ids_string = ",".join(coin_ids)

    response = requests.get(
        f"{BASE_URL}/simple/price", 
        params={
            "ids": ids_string, 
            "vs_currencies": "usd",
            "x_cg_demo_api_key": api_key
        }
    )

    if response.status_code != 200:
        raise RuntimeError(response.status_code)
    
    data = response.json()

    return {coin: float(data[coin]["usd"]) for coin in coin_ids}


class CoinCache:
    """
    A time-aware cache for cryptocurrency prices.

    Stores prices with timestamps and serves them back
    until they expire (based on TTL).
    """

    def __init__(self, ttl_seconds: int = 60):
        """
        Initialize the cache.

        Args:
            ttl_seconds: How many seconds a cached entry stays fresh.
        """
        # TODO: Task 3
        # Set up: ttl_seconds, _store (empty dict), hits (0), misses (0)
        pass

    def put(self, coin_id: str, price: float):
        """
        Store a price in the cache with a timestamp.

        Args:
            coin_id: The coin identifier
            price: The USD price to cache
        """
        # TODO: Task 3
        # Store {"price": price, "timestamp": time.time()} in _store
        pass

    def get(self, coin_id: str):
        """
        Retrieve a cached price if it exists and hasn't expired.

        Args:
            coin_id: The coin identifier

        Returns:
            The cached price as a float, or None if not found / expired.
        """
        # TODO: Task 3 — basic version (just check if key exists)
        # TODO: Task 4 — add TTL check (is the entry still fresh?)
        pass


def get_price_cached(coin_id: str, api_key: str, cache: CoinCache) -> float:
    """
    Fetch a coin's price, using the cache when possible.

    Cache-aside pattern:
    1. Check the cache
    2. On hit — return cached price, skip the API
    3. On miss — fetch from API, store in cache, return price

    Args:
        coin_id: CoinGecko coin identifier
        api_key: CoinGecko Demo API key
        cache: A CoinCache instance

    Returns:
        The USD price as a float.
    """
    # TODO: Task 5
    # 1. Try cache.get(coin_id)
    # 2. If not None, return it (cache hit!)
    # 3. If None, call get_price(), store with cache.put(), return price
    pass