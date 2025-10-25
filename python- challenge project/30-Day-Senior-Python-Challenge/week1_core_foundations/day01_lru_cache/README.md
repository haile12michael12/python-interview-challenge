# Day 1: LRU Cache

## Challenge
Implement an LRU (Least Recently Used) Cache data structure with the following operations:
- `get(key)` - Get the value for a key if it exists, otherwise return -1
- `put(key, value)` - Insert or update a key-value pair

The cache should have a fixed capacity and evict the least recently used item when it's full.

## Advanced Twist
Add Redis-backed persistence to the LRU cache so that data survives application restarts.

## Requirements
- Time complexity for both operations should be O(1)
- Use a combination of hash map and doubly linked list for optimal performance
- For the advanced twist, integrate with Redis for persistence

## Implementation Tips
1. Use Python's `collections.OrderedDict` for a simpler implementation or create your own doubly linked list
2. For Redis integration, consider using the `redis` Python package
3. Handle edge cases like capacity of 0 or 1
4. Consider thread safety if needed for concurrent access

## Testing
Create test cases for:
- Basic get/put operations
- Cache eviction when capacity is exceeded
- Updating existing keys
- Edge cases with small capacities