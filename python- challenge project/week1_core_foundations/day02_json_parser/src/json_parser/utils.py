"""
Utility functions for JSON parser.
"""

import re
from typing import Any, Dict, List, Union


def unescape_string(s: str) -> str:
    """
    Unescape a JSON string.
    
    Args:
        s (str): The escaped JSON string
        
    Returns:
        str: The unescaped string
    """
    # Handle common escape sequences
    escape_map = {
        '\\\\': '\\',
        '\\"': '"',
        '\\/': '/',
        '\\b': '\b',
        '\\f': '\f',
        '\\n': '\n',
        '\\r': '\r',
        '\\t': '\t'
    }
    
    result = s
    for escaped, unescaped in escape_map.items():
        result = result.replace(escaped, unescaped)
    
    # Handle unicode escapes (\uXXXX)
    def unicode_replacer(match):
        try:
            return chr(int(match.group(1), 16))
        except ValueError:
            return match.group(0)  # Return original if invalid
    
    result = re.sub(r'\\u([0-9a-fA-F]{4})', unicode_replacer, result)
    
    return result


def escape_string(s: str) -> str:
    """
    Escape a string for JSON.
    
    Args:
        s (str): The string to escape
        
    Returns:
        str: The escaped string
    """
    escape_map = {
        '\\': '\\\\',
        '"': '\\"',
        '\b': '\\b',
        '\f': '\\f',
        '\n': '\\n',
        '\r': '\\r',
        '\t': '\\t'
    }
    
    result = s
    for char, escaped in escape_map.items():
        result = result.replace(char, escaped)
    
    # Escape control characters
    result = re.sub(r'[\x00-\x1f]', lambda m: f'\\u{ord(m.group(0)):04x}', result)
    
    return f'"{result}"'


def format_json(obj: Any, indent: int = 2) -> str:
    """
    Format a Python object as pretty-printed JSON.
    
    Args:
        obj (Any): The Python object to format
        indent (int): Number of spaces for each indentation level
        
    Returns:
        str: The formatted JSON string
    """
    def _format(value: Any, current_indent: int = 0) -> str:
        spaces = " " * current_indent
        next_spaces = " " * (current_indent + indent)
        
        if value is None:
            return "null"
        elif isinstance(value, bool):
            return "true" if value else "false"
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, str):
            return escape_string(value)
        elif isinstance(value, list):
            if not value:
                return "[]"
            items = [f"{next_spaces}{_format(item, current_indent + indent)}" for item in value]
            return "[\n" + ",\n".join(items) + f"\n{spaces}]"
        elif isinstance(value, dict):
            if not value:
                return "{}"
            items = []
            for key, val in value.items():
                key_str = escape_string(str(key))
                val_str = _format(val, current_indent + indent)
                items.append(f"{next_spaces}{key_str}: {val_str}")
            return "{\n" + ",\n".join(items) + "\n" + spaces + "}"
        else:
            return escape_string(str(value))
    
    return _format(obj)


def validate_json_structure(obj: Any) -> bool:
    """
    Validate that a Python object can be serialized to JSON.
    
    Args:
        obj (Any): The object to validate
        
    Returns:
        bool: True if the object is JSON-serializable, False otherwise
    """
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return True
    elif isinstance(obj, list):
        return all(validate_json_structure(item) for item in obj)
    elif isinstance(obj, dict):
        # Check that all keys are strings and all values are valid
        return all(isinstance(key, str) and validate_json_structure(value) 
                  for key, value in obj.items())
    else:
        return False


def get_json_type(obj: Any) -> str:
    """
    Get the JSON type of a Python object.
    
    Args:
        obj (Any): The Python object
        
    Returns:
        str: The JSON type as a string
    """
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        return "boolean"
    elif isinstance(obj, int):
        return "integer"
    elif isinstance(obj, float):
        return "number"
    elif isinstance(obj, str):
        return "string"
    elif isinstance(obj, list):
        return "array"
    elif isinstance(obj, dict):
        return "object"
    else:
        return "unknown"