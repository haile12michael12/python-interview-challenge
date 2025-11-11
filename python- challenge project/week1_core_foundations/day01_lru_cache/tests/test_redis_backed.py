"""
Tests for the Redis-backed LRU Cache implementation.
"""

import unittest
from lru_cache.redis_backed import RedisLRUCache


class TestRedisLRUCache(unittest.TestCase):
    """Test cases for RedisLRUCache class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cache = RedisLRUCache(3)
    
    def test_put_and_get(self):
        """Test basic put and get operations."""
        self.cache.put("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")
        self.assertIsNone(self.cache.get("nonexistent"))
    
    def test_lru_eviction(self):
        """Test LRU eviction policy."""
        # Fill cache to capacity
        self.cache.put("key1", "value1")
        self.cache.put("key2", "value2")
        self.cache.put("key3", "value3")
        
        # Access key1 to make it recently used
        self.cache.get("key1")
        
        # Add key4, which should evict key2 (least recently used)
        self.cache.put("key4", "value4")
        
        # In our simplified implementation, we only check local cache
        # key2 should be evicted, others should remain
        self.assertIsNone(self.cache.get("key2"))
        self.assertEqual(self.cache.get("key1"), "value1")
        self.assertEqual(self.cache.get("key3"), "value3")
        self.assertEqual(self.cache.get("key4"), "value4")
    
    def test_len_and_contains(self):
        """Test __len__ and __contains__ methods."""
        self.assertEqual(len(self.cache), 0)
        self.assertFalse("key1" in self.cache)
        
        self.cache.put("key1", "value1")
        self.assertEqual(len(self.cache), 1)
        self.assertTrue("key1" in self.cache)


if __name__ == "__main__":
    unittest.main()