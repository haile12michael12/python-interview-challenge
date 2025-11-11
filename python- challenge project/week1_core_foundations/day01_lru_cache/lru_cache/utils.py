"""
Utility functions for LRU Cache implementations.
"""

import json
from typing import Any, Dict


def serialize_cache_stats(cache_obj) -> Dict[str, Any]:
    """
    Serialize cache statistics to a dictionary.
    
    Args:
        cache_obj: Cache object with capacity and length properties
        
    Returns:
        Dictionary with cache statistics
    """
    return {
        "capacity": getattr(cache_obj, 'capacity', None),
        "current_size": len(cache_obj),
        "utilization": len(cache_obj) / getattr(cache_obj, 'capacity', 1) if getattr(cache_obj, 'capacity', 0) > 0 else 0
    }


def format_cache_keys(cache_obj) -> str:
    """
    Format cache keys for display.
    
    Args:
        cache_obj: Cache object with keys() method
        
    Returns:
        Formatted string of cache keys
    """
    try:
        keys = cache_obj.keys()
        if not keys:
            return "[]"
        return "[" + ", ".join(map(str, keys)) + "]"
    except Exception:
        return "[Error retrieving keys]"


def cache_to_dict(cache_obj) -> Dict:
    """
    Convert cache to dictionary representation.
    
    Args:
        cache_obj: Cache object
        
    Returns:
        Dictionary representation of cache
    """
    result = {}
    try:
        # This is a simplified version - actual implementation would depend on cache type
        if hasattr(cache_obj, 'cache'):
            # For OrderedDict-based caches
            if hasattr(cache_obj.cache, 'items'):
                result = dict(cache_obj.cache)
        elif hasattr(cache_obj, 'keys'):
            # For custom implementations, we might need to iterate differently
            for key in cache_obj.keys():
                try:
                    result[key] = cache_obj.get(key)
                except Exception:
                    result[key] = "<Error retrieving value>"
    except Exception:
        pass
    
    return result