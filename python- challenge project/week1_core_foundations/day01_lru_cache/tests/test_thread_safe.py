"""
Tests for the thread-safe LRU Cache implementation.
"""

import unittest
import threading
import time
from lru_cache.thread_safe import ThreadSafeLRUCache


class TestThreadSafeLRUCache(unittest.TestCase):
    """Test cases for ThreadSafeLRUCache class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cache = ThreadSafeLRUCache(3)
    
    def test_put_and_get(self):
        """Test basic put and get operations."""
        self.cache.put("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")
        self.assertIsNone(self.cache.get("nonexistent"))
    
    def test_thread_safety(self):
        """Test thread safety with concurrent access."""
        errors = []
        
        def worker(thread_id):
            try:
                # Each thread puts and gets its own keys
                for i in range(10):
                    key = f"thread{thread_id}_key{i}"
                    value = f"value_{thread_id}_{i}"
                    self.cache.put(key, value)
                    retrieved = self.cache.get(key)
                    if retrieved != value:
                        errors.append(f"Thread {thread_id}: Expected {value}, got {retrieved}")
            except Exception as e:
                errors.append(f"Thread {thread_id} error: {e}")
        
        # Create and start multiple threads
        threads = []
        for i in range(5):
            thread = threading.Thread(target=worker, args=(i,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Check for errors
        self.assertEqual(len(errors), 0, f"Errors occurred: {errors}")
    
    def test_len_and_contains(self):
        """Test __len__ and __contains__ methods."""
        self.assertEqual(len(self.cache), 0)
        self.assertFalse("key1" in self.cache)
        
        self.cache.put("key1", "value1")
        self.assertEqual(len(self.cache), 1)
        self.assertTrue("key1" in self.cache)
    
    def test_concurrent_put_get(self):
        """Test concurrent put and get operations."""
        # Pre-populate cache
        self.cache.put("shared_key", "initial_value")
        
        results = []
        errors = []
        
        def reader():
            try:
                value = self.cache.get("shared_key")
                results.append(value)
            except Exception as e:
                errors.append(f"Reader error: {e}")
        
        def writer():
            try:
                self.cache.put("shared_key", "updated_value")
            except Exception as e:
                errors.append(f"Writer error: {e}")
        
        # Create reader and writer threads
        threads = []
        for _ in range(10):
            reader_thread = threading.Thread(target=reader)
            writer_thread = threading.Thread(target=writer)
            threads.extend([reader_thread, writer_thread])
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Check for errors
        self.assertEqual(len(errors), 0, f"Errors occurred: {errors}")


if __name__ == "__main__":
    unittest.main()