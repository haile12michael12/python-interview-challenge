"""
JSON Serializer for converting Python objects to JSON text.
"""

import json
from typing import Any, Union, Optional
from .errors import JSONParseError


class JSONSerializer:
    """
    Serializer for converting Python objects to JSON text.
    
    This implementation provides a custom JSON serializer that converts
    Python data structures back to JSON format.
    """
    
    def __init__(self):
        """Initialize the JSON serializer."""
        pass
    
    def serialize(self, obj: Any, indent: Optional[int] = None) -> str:
        """
        Serialize a Python object to JSON text.
        
        Args:
            obj (Any): The Python object to serialize
            indent (Optional[int]): Number of spaces for indentation (None for compact)
            
        Returns:
            str: The JSON text representation
            
        Raises:
            JSONParseError: If the object contains non-serializable types
        """
        try:
            # For basic implementation, we can use Python's built-in json module
            # but we'll also provide a custom implementation for educational purposes
            return json.dumps(obj, indent=indent, ensure_ascii=False)
        except (TypeError, ValueError) as e:
            raise JSONParseError(f"Object is not JSON serializable: {e}")
    
    def to_json(self, obj: Any, indent: Optional[int] = None) -> str:
        """
        Convert a Python object to JSON text (custom implementation).
        
        Args:
            obj (Any): The Python object to convert
            indent (Optional[int]): Number of spaces for indentation (None for compact)
            
        Returns:
            str: The JSON text representation
            
        Raises:
            JSONParseError: If the object contains non-serializable types
        """
        try:
            return self._serialize_object(obj, indent=indent or 0, current_indent=0)
        except Exception as e:
            raise JSONParseError(f"Object is not JSON serializable: {e}")
    
    def _serialize_object(self, obj: Any, indent: int, current_indent: int) -> str:
        """
        Recursively serialize a Python object to JSON text.
        
        Args:
            obj (Any): The Python object to serialize
            indent (int): Number of spaces for indentation
            current_indent (int): Current indentation level
            
        Returns:
            str: The JSON text representation
        """
        if obj is None:
            return "null"
        elif isinstance(obj, bool):
            return "true" if obj else "false"
        elif isinstance(obj, (int, float)):
            # Handle special float values
            if isinstance(obj, float):
                if obj != obj:  # NaN
                    raise JSONParseError("NaN is not supported in JSON")
                if obj == float('inf'):
                    raise JSONParseError("Infinity is not supported in JSON")
                if obj == float('-inf'):
                    raise JSONParseError("Negative infinity is not supported in JSON")
            return str(obj)
        elif isinstance(obj, str):
            return self._escape_string(obj)
        elif isinstance(obj, list):
            return self._serialize_list(obj, indent, current_indent)
        elif isinstance(obj, dict):
            return self._serialize_dict(obj, indent, current_indent)
        else:
            raise JSONParseError(f"Object of type {type(obj).__name__} is not JSON serializable")
    
    def _escape_string(self, s: str) -> str:
        """
        Escape a string for JSON.
        
        Args:
            s (str): The string to escape
            
        Returns:
            str: The escaped string
        """
        # Use Python's built-in JSON encoder for string escaping
        return json.dumps(s, ensure_ascii=False)
    
    def _serialize_list(self, lst: list, indent: int, current_indent: int) -> str:
        """
        Serialize a list to JSON array.
        
        Args:
            lst (list): The list to serialize
            indent (int): Number of spaces for indentation
            current_indent (int): Current indentation level
            
        Returns:
            str: The JSON array representation
        """
        if not lst:
            return "[]"
        
        if indent > 0:
            items = []
            new_indent = current_indent + indent
            for item in lst:
                items.append(" " * new_indent + self._serialize_object(item, indent, new_indent))
            return "[\n" + ",\n".join(items) + "\n" + " " * current_indent + "]"
        else:
            items = [self._serialize_object(item, indent, current_indent) for item in lst]
            return "[" + ", ".join(items) + "]"
    
    def _serialize_dict(self, dct: dict, indent: int, current_indent: int) -> str:
        """
        Serialize a dictionary to JSON object.
        
        Args:
            dct (dict): The dictionary to serialize
            indent (int): Number of spaces for indentation
            current_indent (int): Current indentation level
            
        Returns:
            str: The JSON object representation
        """
        if not dct:
            return "{}"
        
        if indent > 0:
            items = []
            new_indent = current_indent + indent
            for key, value in dct.items():
                if not isinstance(key, str):
                    raise JSONParseError(f"Dictionary key must be a string, got {type(key).__name__}")
                key_str = self._escape_string(key)
                value_str = self._serialize_object(value, indent, new_indent)
                items.append(" " * new_indent + f"{key_str}: {value_str}")
            return "{\n" + ",\n".join(items) + "\n" + " " * current_indent + "}"
        else:
            items = []
            for key, value in dct.items():
                if not isinstance(key, str):
                    raise JSONParseError(f"Dictionary key must be a string, got {type(key).__name__}")
                key_str = self._escape_string(key)
                value_str = self._serialize_object(value, indent, current_indent)
                items.append(f"{key_str}: {value_str}")
            return "{" + ", ".join(items) + "}"