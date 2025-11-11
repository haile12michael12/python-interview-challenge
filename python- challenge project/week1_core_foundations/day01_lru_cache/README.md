# Day 1: LRU Cache Implementation

This directory contains multiple implementations of the Least Recently Used (LRU) cache algorithm as part of the 60-Day Senior Python Challenge.

## Project Structure

```
lru_cache_project/
├── lru_cache/
│   ├── __init__.py
│   ├── core.py                    # Core doubly linked list LRU cache
│   ├── simple.py                  # OrderedDict-based LRU
│   ├── redis_backed.py            # Redis-backed persistent LRU
│   ├── thread_safe.py             # Thread-safe wrappers
│   ├── exceptions.py              # Custom exceptions
│   └── utils.py                   # Helper functions
│
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_redis_backed.py
│   ├── test_thread_safe.py
│   └── test_utils.py
│
├── scripts/
│   ├── run_cache_demo.py          # CLI demo runner
│   ├── benchmark.py               # Performance comparison
│   └── redis_init.py              # Redis setup utility
│
├── docs/
│   ├── README.md
│   ├── DESIGN.md                  # Architecture explanation
│   └── API_REFERENCE.md
│
├── requirements.txt               # Dependencies
├── setup.py                       # For pip installation
└── .gitignore
```

## Implementations

### 1. Core LRU Cache (`lru_cache/core.py`)
- Full-featured implementation using doubly linked list
- O(1) time complexity for get/put operations
- Custom doubly linked list implementation

### 2. Simple LRU Cache (`lru_cache/simple.py`)
- Simplified implementation using OrderedDict
- Easier to understand and maintain
- Leverages Python's built-in data structures

### 3. Thread-Safe LRU Cache (`lru_cache/thread_safe.py`)
- Wrapper around core implementation with thread safety
- Uses reentrant locks for synchronization
- Safe for concurrent access

### 4. Redis-Backed LRU Cache (`lru_cache/redis_backed.py`)
- Persistent cache using Redis as backing store
- Local cache for fast access
- Cache-aside pattern implementation

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run demos:
   ```bash
   python scripts/run_cache_demo.py
   ```

3. Run tests:
   ```bash
   python -m unittest discover tests
   ```

4. Run benchmarks:
   ```bash
   python scripts/benchmark.py
   ```

## Learning Objectives

- Understand LRU cache algorithm and its applications
- Implement data structures for optimal performance
- Handle thread safety in concurrent environments
- Design extensible and maintainable code
- Work with persistence layers (Redis)
- Write comprehensive tests and benchmarks

## Related Resources

- [Design Documentation](docs/DESIGN.md)
- [API Reference](docs/API_REFERENCE.md)