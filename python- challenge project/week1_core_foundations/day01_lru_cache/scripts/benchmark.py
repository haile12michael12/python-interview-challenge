"""
Benchmark script for comparing LRU Cache implementations.
"""

import sys
import os
import time
import random
import string

# Add the parent directory to the path so we can import lru_cache
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lru_cache.core import LRUCache
from lru_cache.simple import SimpleLRUCache
from lru_cache.thread_safe import ThreadSafeLRUCache


def generate_random_string(length=10):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def benchmark_cache(cache, num_operations=10000, cache_size=1000):
    """Benchmark a cache implementation."""
    # Generate test data
    test_keys = [generate_random_string() for _ in range(cache_size * 2)]
    test_values = [random.randint(1, 1000000) for _ in range(cache_size * 2)]
    
    start_time = time.time()
    
    # Perform operations
    for i in range(num_operations):
        key = test_keys[i % len(test_keys)]
        value = test_values[i % len(test_values)]
        
        # 70% get operations, 30% put operations
        if random.random() < 0.7:
            cache.get(key)
        else:
            cache.put(key, value)
    
    end_time = time.time()
    return end_time - start_time


def main():
    """Run benchmarks for all cache implementations."""
    print("LRU Cache Performance Benchmark")
    print("=" * 30)
    
    cache_size = 1000
    num_operations = 50000
    
    print(f"Cache size: {cache_size}")
    print(f"Operations: {num_operations}")
    print()
    
    # Benchmark Core LRU Cache
    print("Benchmarking Core LRU Cache...")
    core_cache = LRUCache(cache_size)
    core_time = benchmark_cache(core_cache, num_operations, cache_size)
    print(f"Core LRU Cache: {core_time:.4f} seconds")
    
    # Benchmark Simple LRU Cache
    print("Benchmarking Simple LRU Cache...")
    simple_cache = SimpleLRUCache(cache_size)
    simple_time = benchmark_cache(simple_cache, num_operations, cache_size)
    print(f"Simple LRU Cache: {simple_time:.4f} seconds")
    
    # Benchmark Thread-Safe LRU Cache
    print("Benchmarking Thread-Safe LRU Cache...")
    thread_safe_cache = ThreadSafeLRUCache(cache_size)
    thread_safe_time = benchmark_cache(thread_safe_cache, num_operations, cache_size)
    print(f"Thread-Safe LRU Cache: {thread_safe_time:.4f} seconds")
    
    # Show relative performance
    print()
    print("Performance Comparison:")
    print(f"Simple LRU Cache is {simple_time/core_time:.2f}x the speed of Core LRU Cache")
    print(f"Thread-Safe LRU Cache is {thread_safe_time/core_time:.2f}x the speed of Core LRU Cache")


if __name__ == "__main__":
    main()