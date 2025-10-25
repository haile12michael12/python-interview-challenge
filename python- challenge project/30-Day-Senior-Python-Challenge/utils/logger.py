"""
Logging utilities for the 30-Day Senior Python Challenge.
"""

import logging
import sys
from typing import Optional


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Set up a logger with console handler.
    
    Args:
        name: Name of the logger
        level: Logging level
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent adding multiple handlers if logger already exists
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance.
    
    Args:
        name: Name of the logger. If None, uses the module name.
        
    Returns:
        Logger instance
    """
    if name is None:
        name = __name__
    return setup_logger(name)


# Default logger
logger = get_logger(__name__)