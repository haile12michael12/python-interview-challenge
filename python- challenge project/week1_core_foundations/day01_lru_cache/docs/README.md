# LRU Cache Implementation Project

This project provides multiple implementations of the Least Recently Used (LRU) cache algorithm, each with different trade-offs and use cases.

## Implementations

### 1. Core Implementation (`core.py`)
A full-featured LRU cache implementation using a doubly linked list and hash map for O(1) time complexity.

### 2. Simple Implementation (`simple.py`)
A simplified version using Python's `OrderedDict` for easier understanding.

### 3. Thread-Safe Implementation (`thread_safe.py`)
A thread-safe wrapper around the core implementation using locks.

### 4. Redis-Backed Implementation (`redis_backed.py`)
A persistent LRU cache that uses Redis for storage while maintaining fast local access.

## Features

- Multiple LRU cache implementations with different characteristics
- Comprehensive test suite
- Performance benchmarking tools
- Utility functions for cache statistics and serialization
- Thread-safe operations
- Extensible design

## Usage

```python
from lru_cache.core import LRUCache

# Create a cache with capacity of 100 items
cache = LRUCache(100)

# Add items
cache.put("key1", "value1")
cache.put("key2", "value2")

# Retrieve items
value = cache.get("key1")

# Check cache size
print(len(cache))
```

## Running Tests

```bash
python -m unittest discover tests
```

## Running Demos

```bash
python scripts/run_cache_demo.py
```

## Benchmarking

```bash
python scripts/benchmark.py
```