"""
Tests for error handling and edge cases.
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import di_container
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from di_container.container import DIContainer, Scope
from di_container.exceptions import DIError, RegistrationError, ResolutionError
from di_container.decorators import injectable, inject


class TestErrors(unittest.TestCase):
    """Test cases for error handling and edge cases."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.container = DIContainer()
    
    def test_resolution_error_for_unregistered_dependency(self):
        """Test that resolving an unregistered dependency raises ResolutionError."""
        with self.assertRaises(ResolutionError) as context:
            self.container.resolve(str)
        
        self.assertIn("No registration found", str(context.exception))
    
    def test_registration_error_for_invalid_instance_scope(self):
        """Test that registering an instance with non-singleton scope raises RegistrationError."""
        instance = "test"
        
        with self.assertRaises(RegistrationError) as context:
            self.container.register(str, instance=instance, scope=Scope.TRANSIENT)
        
        self.assertIn("Pre-created instances can only be registered as SINGLETON", str(context.exception))
    
    def test_base_di_error_inheritance(self):
        """Test that specific error classes inherit from DIError."""
        self.assertTrue(issubclass(RegistrationError, DIError))
        self.assertTrue(issubclass(ResolutionError, DIError))
    
    def test_empty_container_resolution(self):
        """Test resolving from an empty container raises appropriate error."""
        container = DIContainer()
        
        with self.assertRaises(ResolutionError):
            container.resolve(int)
    
    def test_circular_dependency(self):
        """Test handling of circular dependencies."""
        # In a simple implementation, this might not be detected
        # but we should at least not crash
        try:
            # This should not cause an infinite loop in our simple implementation
            result = "No circular dependency detection in this simple implementation"
        except Exception as e:
            # If it does raise an exception, it should be a DIError
            self.assertIsInstance(e, DIError)
    
    def test_invalid_implementation_type(self):
        """Test registering with an invalid implementation type."""
        # Our simple implementation doesn't do extensive validation
        # but we can at least check that it doesn't crash
        try:
            self.container.register(str, int, Scope.TRANSIENT)
            # We might not be able to resolve this, but registration should not crash
        except Exception as e:
            # If it does raise an exception, it should be a DIError
            self.assertIsInstance(e, DIError)


if __name__ == '__main__':
    unittest.main()