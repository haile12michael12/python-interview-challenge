# LRU Cache API Reference

## Core Module

### LRUCache

```python
class LRUCache(capacity: int)
```

**Parameters:**
- `capacity` (int): Maximum number of items the cache can hold

#### Methods

##### get(key)
```python
get(key) -> Optional[Any]
```
Get value for key from cache.

**Parameters:**
- `key`: Key to look up

**Returns:**
- Value associated with key, or None if key not found

##### put(key, value)
```python
put(key, value) -> None
```
Put key-value pair in cache.

**Parameters:**
- `key`: Key to store
- `value`: Value to store

##### keys()
```python
keys() -> List[Any]
```
Return all keys in cache (most recently used first).

**Returns:**
- List of keys in order of most recently used

#### Special Methods

##### __len__()
```python
__len__() -> int
```
Return current number of items in cache.

##### __contains__(key)
```python
__contains__(key) -> bool
```
Check if key exists in cache.

**Parameters:**
- `key`: Key to check

**Returns:**
- True if key exists, False otherwise

## Simple Module

### SimpleLRUCache

```python
class SimpleLRUCache(capacity: int)
```

**Parameters:**
- `capacity` (int): Maximum number of items the cache can hold

*All methods are identical to LRUCache*

## Thread-Safe Module

### ThreadSafeLRUCache

```python
class ThreadSafeLRUCache(capacity: int)
```

**Parameters:**
- `capacity` (int): Maximum number of items the cache can hold

*All methods are identical to LRUCache but with thread safety*

## Redis-Backed Module

### RedisLRUCache

```python
class RedisLRUCache(capacity: int)
```

**Parameters:**
- `capacity` (int): Maximum number of items the cache can hold

*All methods are identical to LRUCache with Redis persistence*

## Exceptions Module

### LRUCacheError
```python
class LRUCacheError(Exception)
```
Base exception for LRU Cache errors.

### InvalidCapacityError
```python
class InvalidCapacityError(LRUCacheError)
```
Raised when an invalid capacity is provided.

### CacheKeyError
```python
class CacheKeyError(LRUCacheError)
```
Raised when there's an issue with cache keys.

### CacheValueError
```python
class CacheValueError(LRUCacheError)
```
Raised when there's an issue with cache values.

## Utils Module

### serialize_cache_stats
```python
serialize_cache_stats(cache_obj) -> Dict[str, Any]
```
Serialize cache statistics to a dictionary.

**Parameters:**
- `cache_obj`: Cache object with capacity and length properties

**Returns:**
- Dictionary with cache statistics

### format_cache_keys
```python
format_cache_keys(cache_obj) -> str
```
Format cache keys for display.

**Parameters:**
- `cache_obj`: Cache object with keys() method

**Returns:**
- Formatted string of cache keys

### cache_to_dict
```python
cache_to_dict(cache_obj) -> Dict
```
Convert cache to dictionary representation.

**Parameters:**
- `cache_obj`: Cache object

**Returns:**
- Dictionary representation of cache