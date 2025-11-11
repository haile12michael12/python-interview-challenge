"""
Core LRU Cache implementation using doubly linked list.
"""

from typing import Optional


class Node:
    """Doubly linked list node for LRU cache."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None


class LRUCache:
    """
    LRU (Least Recently Used) Cache implementation using doubly linked list and hash map.
    
    Time Complexity:
    - get: O(1)
    - put: O(1)
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity (int): Maximum number of items the cache can hold
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
            
        self.capacity = capacity
        self.cache = {}  # Hash map for O(1) lookup
        
        # Dummy head and tail nodes for doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        """
        Get value for key from cache.
        
        Args:
            key: Key to look up
            
        Returns:
            Value associated with key, or None if key not found
        """
        node = self.cache.get(key)
        if not node:
            return None
            
        # Move accessed node to front (most recently used)
        self._remove_node(node)
        self._add_node_to_front(node)
        
        return node.value
    
    def put(self, key, value):
        """
        Put key-value pair in cache.
        
        Args:
            key: Key to store
            value: Value to store
        """
        node = self.cache.get(key)
        if node:
            # Update existing node
            node.value = value
            self._remove_node(node)
            self._add_node_to_front(node)
        else:
            # Add new node
            if len(self.cache) >= self.capacity:
                # Remove least recently used item (tail)
                lru_node = self.tail.prev
                if lru_node is not None and lru_node != self.head:
                    self._remove_node(lru_node)
                    del self.cache[lru_node.key]
            
            # Add new node to front
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node_to_front(new_node)
    
    def _remove_node(self, node):
        """Remove node from doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_node_to_front(self, node):
        """Add node to front of doubly linked list (most recently used)."""
        if self.head.next is not None:
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
    
    def __len__(self):
        """Return current number of items in cache."""
        return len(self.cache)
    
    def __contains__(self, key):
        """Check if key exists in cache."""
        return key in self.cache
    
    def keys(self):
        """Return all keys in cache (most recently used first)."""
        keys = []
        current = self.head.next
        while current is not None and current != self.tail:
            if current.key is not None:
                keys.append(current.key)
            current = current.next
        return keys