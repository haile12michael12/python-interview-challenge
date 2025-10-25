"""
Configuration loader utilities for the 30-Day Senior Python Challenge.
"""

import json
import os
from typing import Any, Dict, Optional
from .logger import get_logger

logger = get_logger(__name__)


class ConfigLoader:
    """Load and manage configuration from various sources."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the ConfigLoader.
        
        Args:
            config_path: Path to the configuration file
        """
        self.config_path = config_path or 'config.json'
        self._config: Dict[str, Any] = {}
        self._load_config()
    
    def _load_config(self) -> None:
        """Load configuration from file."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    self._config = json.load(f)
                logger.info(f"Configuration loaded from {self.config_path}")
            except Exception as e:
                logger.error(f"Failed to load configuration: {e}")
        else:
            logger.warning(f"Configuration file {self.config_path} not found")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self._config[key] = value
    
    def save(self) -> None:
        """Save configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self._config, f, indent=2)
            logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            logger.error(f"Failed to save configuration: {e}")


# Global config loader instance
config_loader = ConfigLoader()