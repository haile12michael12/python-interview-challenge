# LRU Cache Design Documentation

## Overview

This document explains the design and implementation of various LRU (Least Recently Used) cache algorithms provided in this project.

## Core Implementation Design

### Data Structures

1. **Hash Map**: Provides O(1) lookup for keys
2. **Doubly Linked List**: Maintains order of usage for LRU eviction

### Algorithm

1. **Get Operation**:
   - Look up key in hash map: O(1)
   - If found, move node to front of list (most recently used): O(1)
   - Return value

2. **Put Operation**:
   - Check if key exists in hash map: O(1)
   - If exists, update value and move to front: O(1)
   - If not exists:
     - If cache is full, remove tail node (LRU item): O(1)
     - Add new node to front of list: O(1)
     - Add entry to hash map: O(1)

### Time Complexity

- Get: O(1)
- Put: O(1)

### Space Complexity

- O(N) where N is the cache capacity

## Simple Implementation Design

### Data Structures

1. **OrderedDict**: Combines hash map and doubly linked list functionality

### Algorithm

1. **Get Operation**:
   - Look up key in OrderedDict: O(1)
   - Move key to end (most recently used): O(1)
   - Return value

2. **Put Operation**:
   - If key exists, move to end: O(1)
   - If cache is full, remove first item (LRU): O(1)
   - Add/update key-value pair: O(1)

### Trade-offs

- Simpler implementation
- Relies on Python's built-in OrderedDict
- Slightly higher overhead due to OrderedDict's additional features

## Thread-Safe Implementation Design

### Synchronization

- Uses `threading.RLock()` for reentrant locking
- All public methods are wrapped with lock acquisition/release

### Trade-offs

- Ensures thread safety
- Adds overhead due to locking
- May become a bottleneck under high contention

## Redis-Backed Implementation Design

### Architecture

- Local LRU cache for fast access
- Redis for persistence
- Cache-aside pattern for data retrieval

### Data Flow

1. **Get Operation**:
   - Check local cache first
   - If not found, check Redis
   - If found in Redis, populate local cache

2. **Put Operation**:
   - Store in local cache
   - Asynchronously store in Redis

### Trade-offs

- Persistence across application restarts
- Higher latency due to Redis operations
- Increased complexity
- Network dependency

## Exception Handling

Custom exceptions are defined in [exceptions.py](file://c:\new-2-month\ptyhon-interview-challenge\python-%20challenge%20project\week1_core_foundations\day01_lru_cache\lru_cache\exceptions.py) to provide clear error messages and categorization:

- `LRUCacheError`: Base exception
- `InvalidCapacityError`: For invalid capacity values
- `CacheKeyError`: For key-related issues
- `CacheValueError`: For value-related issues