"""
Thread-safe wrappers for LRU Cache implementations.
"""

import threading
from typing import Any, Optional
from .core import LRUCache


class ThreadSafeLRUCache:
    """
    Thread-safe wrapper for LRUCache.
    
    This implementation uses a lock to ensure thread safety
    for all cache operations.
    """
    
    def __init__(self, capacity: int):
        """
        Initialize thread-safe LRU cache with given capacity.
        
        Args:
            capacity (int): Maximum number of items the cache can hold
        """
        self.cache = LRUCache(capacity)
        self.lock = threading.RLock()  # Reentrant lock
    
    def get(self, key) -> Optional[Any]:
        """
        Thread-safe get operation.
        
        Args:
            key: Key to look up
            
        Returns:
            Value associated with key, or None if key not found
        """
        with self.lock:
            return self.cache.get(key)
    
    def put(self, key, value) -> None:
        """
        Thread-safe put operation.
        
        Args:
            key: Key to store
            value: Value to store
        """
        with self.lock:
            self.cache.put(key, value)
    
    def __len__(self) -> int:
        """Thread-safe length operation."""
        with self.lock:
            return len(self.cache)
    
    def __contains__(self, key) -> bool:
        """Thread-safe contains operation."""
        with self.lock:
            return key in self.cache
    
    def keys(self):
        """Thread-safe keys operation."""
        with self.lock:
            return self.cache.keys()