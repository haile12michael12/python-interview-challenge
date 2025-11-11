"""
Simple LRU Cache implementation using OrderedDict.
"""

from collections import OrderedDict


class SimpleLRUCache:
    """
    Simple LRU (Least Recently Used) Cache implementation using OrderedDict.
    
    This is a simpler implementation that relies on OrderedDict's built-in
    functionality for maintaining order and moving items to end.
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity (int): Maximum number of items the cache can hold
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
            
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        """
        Get value for key from cache.
        
        Args:
            key: Key to look up
            
        Returns:
            Value associated with key, or None if key not found
        """
        if key not in self.cache:
            return None
            
        # Move accessed key to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """
        Put key-value pair in cache.
        
        Args:
            key: Key to store
            value: Value to store
        """
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used item (first item)
            self.cache.popitem(last=False)
        
        # Add/update key-value pair
        self.cache[key] = value
    
    def __len__(self):
        """Return current number of items in cache."""
        return len(self.cache)
    
    def __contains__(self, key):
        """Check if key exists in cache."""
        return key in self.cache
    
    def keys(self):
        """Return all keys in cache (most recently used first)."""
        return list(reversed(list(self.cache.keys())))