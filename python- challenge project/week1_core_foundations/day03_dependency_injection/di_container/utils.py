"""
Utility functions for Dependency Injection Container.
"""

import inspect
from typing import Any, Callable, Dict, List, Type, get_type_hints


def get_constructor_parameters(cls: Type[Any]) -> Dict[str, Type[Any]]:
    """
    Get the constructor parameters of a class.
    
    Args:
        cls: The class to inspect
        
    Returns:
        A dictionary mapping parameter names to their types
    """
    try:
        # Get the constructor
        constructor = cls.__init__
        
        # Get type hints
        type_hints = get_type_hints(constructor)
        
        # Get the signature
        signature = inspect.signature(constructor)
        
        # Build parameter information
        parameters = {}
        for name, param in signature.parameters.items():
            # Skip 'self' parameter
            if name == 'self':
                continue
                
            # Get the type hint, or use Any if not specified
            param_type = type_hints.get(name, Any)
            parameters[name] = param_type
            
        return parameters
    except Exception:
        # If we can't inspect the constructor, return empty dict
        return {}


def is_injectable(cls: Type[Any]) -> bool:
    """
    Check if a class is marked as injectable.
    
    Args:
        cls: The class to check
        
    Returns:
        True if the class is marked as injectable, False otherwise
    """
    return getattr(cls, '__injectable__', False)


def get_injectable_dependencies(func: Callable[..., Any]) -> Dict[str, Type[Any]]:
    """
    Get injectable dependencies for a function or method.
    
    Args:
        func: The function to inspect
        
    Returns:
        A dictionary mapping parameter names to their dependency types
    """
    return getattr(func, '__inject_dependencies__', {})


def has_default_value(func: Callable[..., Any], param_name: str) -> bool:
    """
    Check if a parameter has a default value.
    
    Args:
        func: The function to inspect
        param_name: The name of the parameter
        
    Returns:
        True if the parameter has a default value, False otherwise
    """
    try:
        signature = inspect.signature(func)
        param = signature.parameters.get(param_name)
        return param is not None and param.default is not param.empty
    except Exception:
        return False