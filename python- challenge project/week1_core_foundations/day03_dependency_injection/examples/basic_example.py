"""
Basic example of Dependency Injection Container usage.
"""

import sys
import os

# Add the parent directory to the path so we can import di_container
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from di_container.container import DIContainer, Scope
from di_container.exceptions import DIError


# Define some example classes
class DatabaseInterface:
    """Database interface."""
    def connect(self):
        raise NotImplementedError


class MySQLDatabase(DatabaseInterface):
    """MySQL database implementation."""
    def connect(self):
        return "Connected to MySQL database"


class UserService:
    """User service that depends on a database."""
    def __init__(self, database: DatabaseInterface):
        self.database = database
    
    def get_user_data(self):
        connection = self.database.connect()
        return f"User data retrieved using {connection}"


def main():
    """Run basic DI example."""
    print("Basic Dependency Injection Example")
    print("=" * 30)
    
    # Create container
    container = DIContainer()
    
    # Register dependencies
    container.register(DatabaseInterface, MySQLDatabase, Scope.SINGLETON)
    container.register(UserService, UserService, Scope.TRANSIENT)
    
    # Resolve dependencies
    try:
        user_service = container.resolve(UserService)
        result = user_service.get_user_data()
        print(result)
        
        # Resolve again to show singleton behavior
        db1 = container.resolve(DatabaseInterface)
        db2 = container.resolve(DatabaseInterface)
        print(f"Same database instance: {db1 is db2}")
        
    except DIError as e:
        print(f"DI Error: {e}")


if __name__ == "__main__":
    main()