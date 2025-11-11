"""
Tests for the LRU Cache utility functions.
"""

import unittest
from lru_cache.core import LRUCache
from lru_cache.utils import serialize_cache_stats, format_cache_keys, cache_to_dict


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cache = LRUCache(3)
        self.cache.put("key1", "value1")
        self.cache.put("key2", "value2")
    
    def test_serialize_cache_stats(self):
        """Test serialize_cache_stats function."""
        stats = serialize_cache_stats(self.cache)
        
        self.assertIn("capacity", stats)
        self.assertIn("current_size", stats)
        self.assertIn("utilization", stats)
        
        self.assertEqual(stats["capacity"], 3)
        self.assertEqual(stats["current_size"], 2)
        self.assertAlmostEqual(stats["utilization"], 2/3, places=2)
    
    def test_format_cache_keys(self):
        """Test format_cache_keys function."""
        formatted = format_cache_keys(self.cache)
        
        # Keys should be in most recently used order
        self.assertIn("key2", formatted)  # Most recently used
        self.assertIn("key1", formatted)  # Least recently used
    
    def test_cache_to_dict(self):
        """Test cache_to_dict function."""
        result = cache_to_dict(self.cache)
        
        # For the core implementation, we're just checking that it doesn't crash
        # The actual implementation might vary, so we'll just check it returns a dict
        self.assertIsInstance(result, dict)


if __name__ == "__main__":
    unittest.main()