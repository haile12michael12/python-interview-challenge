"""
Tests for decorator-based autowiring.
"""

import unittest
import sys
import os

# Add the parent directory to the path so we can import di_container
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from di_container.container import DIContainer, Scope
from di_container.decorators import injectable, inject
from di_container.exceptions import ResolutionError


@injectable
class RepositoryInterface:
    """Repository interface."""
    def get_data(self):
        raise NotImplementedError


@injectable
class DatabaseRepository(RepositoryInterface):
    """Database repository implementation."""
    def get_data(self):
        return "Data from database"


@injectable
class CacheRepository(RepositoryInterface):
    """Cache repository implementation."""
    def get_data(self):
        return "Data from cache"


@injectable
class BusinessService:
    """Business service that depends on a repository."""
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository
    
    def process_data(self):
        return f"Processing: {self.repository.get_data()}"


@inject(repository=RepositoryInterface)
def create_business_service(repository):
    """Factory function to create business service."""
    return BusinessService(repository)


class TestAutowire(unittest.TestCase):
    """Test cases for decorator-based autowiring."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.container = DIContainer()
    
    def test_injectable_decorator(self):
        """Test that @injectable decorator marks classes correctly."""
        self.assertTrue(hasattr(DatabaseRepository, '__injectable__'))
        self.assertTrue(getattr(DatabaseRepository, '__injectable__', False))
    
    def test_inject_decorator(self):
        """Test that @inject decorator stores dependency information."""
        self.assertTrue(hasattr(create_business_service, '__inject_dependencies__'))
        dependencies = getattr(create_business_service, '__inject_dependencies__', {})
        self.assertIn('repository', dependencies)
        self.assertEqual(dependencies['repository'], RepositoryInterface)
    
    def test_autowire_resolution(self):
        """Test autowiring dependencies."""
        # Register dependencies
        self.container.register(RepositoryInterface, DatabaseRepository, Scope.SINGLETON)
        self.container.register(BusinessService, create_business_service, Scope.TRANSIENT)
        
        # Resolve service
        service = self.container.resolve(BusinessService)
        result = service.process_data()
        
        self.assertIsInstance(service, BusinessService)
        self.assertIn("Processing: Data from database", result)
    
    def test_switching_implementations(self):
        """Test switching between different implementations."""
        # Register cache repository instead
        self.container.register(RepositoryInterface, CacheRepository, Scope.SINGLETON)
        self.container.register(BusinessService, create_business_service, Scope.TRANSIENT)
        
        # Resolve service
        service = self.container.resolve(BusinessService)
        result = service.process_data()
        
        self.assertIn("Processing: Data from cache", result)


if __name__ == '__main__':
    unittest.main()