"""
Demo script for LRU Cache implementations.
"""

import sys
import os

# Add the parent directory to the path so we can import lru_cache
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lru_cache.core import LRUCache
from lru_cache.simple import SimpleLRUCache
from lru_cache.thread_safe import ThreadSafeLRUCache
from lru_cache.utils import serialize_cache_stats, format_cache_keys


def demo_core_lru_cache():
    """Demonstrate the core LRU cache implementation."""
    print("=== Core LRU Cache Demo ===")
    cache = LRUCache(3)
    
    # Add some items
    cache.put("A", 1)
    cache.put("B", 2)
    cache.put("C", 3)
    
    print(f"Cache after adding A, B, C: {format_cache_keys(cache)}")
    
    # Access A to make it recently used
    print(f"Accessing A: {cache.get('A')}")
    print(f"Cache after accessing A: {format_cache_keys(cache)}")
    
    # Add D, which should evict B (least recently used)
    cache.put("D", 4)
    print(f"Cache after adding D (B should be evicted): {format_cache_keys(cache)}")
    
    # Show stats
    stats = serialize_cache_stats(cache)
    print(f"Cache stats: {stats}")
    print()


def demo_simple_lru_cache():
    """Demonstrate the simple LRU cache implementation."""
    print("=== Simple LRU Cache Demo ===")
    cache = SimpleLRUCache(3)
    
    # Add some items
    cache.put("X", 10)
    cache.put("Y", 20)
    cache.put("Z", 30)
    
    print(f"Cache after adding X, Y, Z: {cache.keys()}")
    
    # Access X to make it recently used
    print(f"Accessing X: {cache.get('X')}")
    print(f"Cache after accessing X: {cache.keys()}")
    
    # Add W, which should evict Y (least recently used)
    cache.put("W", 40)
    print(f"Cache after adding W (Y should be evicted): {cache.keys()}")
    
    # Show stats
    stats = serialize_cache_stats(cache)
    print(f"Cache stats: {stats}")
    print()


def demo_thread_safe_lru_cache():
    """Demonstrate the thread-safe LRU cache implementation."""
    print("=== Thread-Safe LRU Cache Demo ===")
    cache = ThreadSafeLRUCache(3)
    
    # Add some items
    cache.put("T1", "Thread1")
    cache.put("T2", "Thread2")
    cache.put("T3", "Thread3")
    
    print(f"Cache after adding T1, T2, T3: {cache.keys()}")
    
    # Access T1 to make it recently used
    print(f"Accessing T1: {cache.get('T1')}")
    print(f"Cache after accessing T1: {cache.keys()}")
    
    # Add T4, which should evict T2 (least recently used)
    cache.put("T4", "Thread4")
    print(f"Cache after adding T4 (T2 should be evicted): {cache.keys()}")
    
    # Show stats
    stats = serialize_cache_stats(cache)
    print(f"Cache stats: {stats}")
    print()


def main():
    """Run all demos."""
    print("LRU Cache Implementation Demos")
    print("=" * 30)
    
    demo_core_lru_cache()
    demo_simple_lru_cache()
    demo_thread_safe_lru_cache()
    
    print("All demos completed!")


if __name__ == "__main__":
    main()