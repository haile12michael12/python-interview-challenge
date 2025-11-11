"""
Decorators for Dependency Injection Container.
"""

from typing import Any, Callable, Type, TypeVar
import functools

T = TypeVar('T')


def injectable(cls: Type[T]) -> Type[T]:
    """
    Decorator to mark a class as injectable.
    
    Args:
        cls: The class to mark as injectable
        
    Returns:
        The same class, marked as injectable
    """
    # In a real implementation, we might store metadata about the class
    # For now, we'll just return the class as-is
    setattr(cls, '__injectable__', True)
    return cls


def inject(**dependencies: Type[Any]) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator to inject dependencies into a function or method.
    
    Args:
        **dependencies: Keyword arguments mapping parameter names to dependency types
        
    Returns:
        A decorator function
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # In a real implementation, we would resolve dependencies and inject them
            # For now, we'll just call the function as-is
            return func(*args, **kwargs)
        # Store dependency information for later use
        setattr(wrapper, '__inject_dependencies__', dependencies)
        return wrapper
    return decorator