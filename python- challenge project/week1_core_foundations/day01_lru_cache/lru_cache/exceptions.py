"""
Custom exceptions for LRU Cache implementations.
"""


class LRUCacheError(Exception):
    """Base exception for LRU Cache errors."""
    pass


class InvalidCapacityError(LRUCacheError):
    """Raised when an invalid capacity is provided."""
    pass


class CacheKeyError(LRUCacheError):
    """Raised when there's an issue with cache keys."""
    pass


class CacheValueError(LRUCacheError):
    """Raised when there's an issue with cache values."""
    pass