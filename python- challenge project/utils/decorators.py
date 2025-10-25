"""
Custom decorators for the 30-Day Senior Python Challenge.
"""

import functools
import time
from typing import Any, Callable, TypeVar, cast
from .logger import get_logger

logger = get_logger(__name__)

T = TypeVar('T')


def timing_decorator(func: Callable[..., T]) -> Callable[..., T]:
    """
    Decorator to measure execution time of a function.
    
    Args:
        func: Function to decorate
        
    Returns:
        Decorated function
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return cast(Callable[..., T], wrapper)


def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """
    Decorator to retry a function on exception.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between retries in seconds
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_exception: Exception = Exception("Unknown error")
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(
                        f"Attempt {attempt + 1} failed for {func.__name__}: {e}"
                    )
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            logger.error(
                f"All {max_attempts} attempts failed for {func.__name__}"
            )
            raise last_exception
        return cast(Callable[..., T], wrapper)
    return decorator


def singleton(cls: type) -> type:
    """
    Decorator to make a class a singleton.
    
    Args:
        cls: Class to decorate
        
    Returns:
        Singleton class
    """
    instances: dict[type, Any] = {}
    
    @functools.wraps(cls)
    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return cast(type, get_instance)