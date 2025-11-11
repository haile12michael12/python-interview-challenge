"""
Tests for the core Dependency Injection Container.
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import di_container
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from di_container.container import DIContainer, Scope
from di_container.exceptions import RegistrationError, ResolutionError


class TestService:
    """Test service for dependency injection."""
    def __init__(self):
        self.value = "test"


class TestDIContainer(unittest.TestCase):
    """Test cases for DIContainer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.container = DIContainer()
    
    def test_register_and_resolve_transient(self):
        """Test registering and resolving a transient dependency."""
        self.container.register(TestService, TestService, Scope.TRANSIENT)
        
        # Resolve twice - should get different instances
        service1 = self.container.resolve(TestService)
        service2 = self.container.resolve(TestService)
        
        self.assertIsInstance(service1, TestService)
        self.assertIsInstance(service2, TestService)
        self.assertIsNot(service1, service2)
    
    def test_register_and_resolve_singleton(self):
        """Test registering and resolving a singleton dependency."""
        self.container.register(TestService, TestService, Scope.SINGLETON)
        
        # Resolve twice - should get the same instance
        service1 = self.container.resolve(TestService)
        service2 = self.container.resolve(TestService)
        
        self.assertIsInstance(service1, TestService)
        self.assertIsInstance(service2, TestService)
        self.assertIs(service1, service2)
    
    def test_register_instance(self):
        """Test registering a pre-created instance."""
        instance = TestService()
        instance.value = "pre-created"
        
        self.container.register(TestService, instance=instance, scope=Scope.SINGLETON)
        
        # Resolve - should get the same instance
        service = self.container.resolve(TestService)
        
        self.assertIs(service, instance)
        self.assertEqual(service.value, "pre-created")
    
    def test_resolve_unregistered_dependency(self):
        """Test resolving an unregistered dependency raises an error."""
        with self.assertRaises(ResolutionError):
            self.container.resolve(TestService)
    
    def test_register_instance_with_non_singleton_scope(self):
        """Test that registering an instance with non-singleton scope raises an error."""
        instance = TestService()
        
        with self.assertRaises(RegistrationError):
            self.container.register(TestService, instance=instance, scope=Scope.TRANSIENT)
    
    def test_clear_container(self):
        """Test clearing all registrations and singletons."""
        self.container.register(TestService, TestService, Scope.SINGLETON)
        service1 = self.container.resolve(TestService)
        
        self.container.clear()
        
        # After clearing, resolving should fail
        with self.assertRaises(ResolutionError):
            self.container.resolve(TestService)


if __name__ == '__main__':
    unittest.main()