"""
Challenge 3: LFU Cache

Problem Description:
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

Example:
Input:
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Constraints:
- 1 <= capacity <= 10^4
- 0 <= key <= 10^5
- 0 <= value <= 10^9
- At most 2 * 10^5 calls will be made to get and put.

Approach:
Use a combination of hash maps and doubly linked lists to maintain O(1) time complexity for both operations.
"""

class LFUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LFU Cache with given capacity.
        
        Args:
            capacity (int): Maximum number of items the cache can hold
        """
        # Your implementation here
        pass

    def get(self, key: int) -> int:
        """
        Get the value of the key if it exists in the cache, otherwise return -1.
        
        Args:
            key (int): Key to retrieve value for
            
        Returns:
            int: Value associated with key, or -1 if key doesn't exist
        """
        # Your implementation here
        return -1  # Placeholder return to satisfy type checker

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value of the key.
        
        Args:
            key (int): Key to insert or update
            value (int): Value to associate with key
        """
        # Your implementation here
        pass

# Test cases
if __name__ == "__main__":
    # Test case based on example
    lfu = LFUCache(2)
    lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
    print(f"get(1): {lfu.get(1)}")  # return 1; cache=[1,2], cnt(1)=2, cnt(2)=1
    lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2; cache=[3,1], cnt(3)=1, cnt(1)=2
    print(f"get(2): {lfu.get(2)}")  # return -1 (not found)
    print(f"get(3): {lfu.get(3)}")  # return 3; cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4)   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1; cache=[4,3], cnt(4)=1, cnt(3)=2
    print(f"get(1): {lfu.get(1)}")  # return -1 (not found)
    print(f"get(3): {lfu.get(3)}")  # return 3; cache=[3,4], cnt(3)=3, cnt(4)=2
    print(f"get(4): {lfu.get(4)}")  # return 4; cache=[4,3], cnt(4)=3, cnt(3)=3