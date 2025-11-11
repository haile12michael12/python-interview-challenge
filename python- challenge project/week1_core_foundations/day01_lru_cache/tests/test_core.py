"""
Tests for the core LRU Cache implementation.
"""

import unittest
from lru_cache.core import LRUCache


class TestLRUCache(unittest.TestCase):
    """Test cases for LRUCache class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cache = LRUCache(3)
    
    def test_init_with_invalid_capacity(self):
        """Test initialization with invalid capacity."""
        with self.assertRaises(ValueError):
            LRUCache(0)
        
        with self.assertRaises(ValueError):
            LRUCache(-1)
    
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
        
        # key2 should be evicted, others should remain
        self.assertIsNone(self.cache.get("key2"))
        self.assertEqual(self.cache.get("key1"), "value1")
        self.assertEqual(self.cache.get("key3"), "value3")
        self.assertEqual(self.cache.get("key4"), "value4")
    
    def test_update_existing_key(self):
        """Test updating existing key."""
        self.cache.put("key1", "value1")
        self.cache.put("key1", "updated_value1")
        self.assertEqual(self.cache.get("key1"), "updated_value1")
    
    def test_len_and_contains(self):
        """Test __len__ and __contains__ methods."""
        self.assertEqual(len(self.cache), 0)
        self.assertFalse("key1" in self.cache)
        
        self.cache.put("key1", "value1")
        self.assertEqual(len(self.cache), 1)
        self.assertTrue("key1" in self.cache)
        
        self.cache.put("key2", "value2")
        self.assertEqual(len(self.cache), 2)
        self.assertTrue("key2" in self.cache)
    
    def test_keys_method(self):
        """Test keys method returns keys in correct order."""
        self.cache.put("key1", "value1")
        self.cache.put("key2", "value2")
        self.cache.put("key3", "value3")
        
        # Keys should be returned in most recently used order
        keys = self.cache.keys()
        self.assertEqual(len(keys), 3)
        self.assertEqual(keys[0], "key3")  # Most recently used
        self.assertEqual(keys[1], "key2")
        self.assertEqual(keys[2], "key1")  # Least recently used


if __name__ == "__main__":
    unittest.main()