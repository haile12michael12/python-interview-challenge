"""
Core Dependency Injection Container implementation.
"""

from typing import Any, Dict, Type, TypeVar, Callable, Optional, Union
from enum import Enum
from .exceptions import RegistrationError, ResolutionError

T = TypeVar('T')


class Scope(Enum):
    """Enumeration of dependency scopes."""
    SINGLETON = "singleton"
    TRANSIENT = "transient"
    REQUEST = "request"


class DIContainer:
    """
    Core Dependency Injection Container.
    
    Manages registration and resolution of dependencies with different scopes.
    """
    
    def __init__(self):
        """Initialize the DI container."""
        self._registrations: Dict[Type, Dict[str, Any]] = {}
        self._singletons: Dict[Type, Any] = {}
    
    def register(
        self,
        interface: Type[T],
        implementation: Optional[Union[Type[T], Callable[[], T]]] = None,
        scope: Scope = Scope.TRANSIENT,
        instance: Optional[T] = None
    ) -> None:
        """
        Register a dependency in the container.
        
        Args:
            interface: The interface or type to register
            implementation: The implementation type or factory function
            scope: The scope of the dependency (SINGLETON, TRANSIENT, REQUEST)
            instance: A pre-created instance to register
            
        Raises:
            RegistrationError: If registration parameters are invalid
        """
        if instance is not None:
            # Register a pre-created instance
            if scope != Scope.SINGLETON:
                raise RegistrationError("Pre-created instances can only be registered as SINGLETON scope")
            self._singletons[interface] = instance
            self._registrations[interface] = {
                'implementation': lambda: instance,
                'scope': scope
            }
        elif implementation is not None:
            # Register an implementation type or factory
            self._registrations[interface] = {
                'implementation': implementation,
                'scope': scope
            }
        else:
            # Register the interface as its own implementation
            self._registrations[interface] = {
                'implementation': interface,
                'scope': scope
            }
    
    def resolve(self, interface: Type[T]) -> T:
        """
        Resolve a dependency from the container.
        
        Args:
            interface: The interface or type to resolve
            
        Returns:
            The resolved instance
            
        Raises:
            ResolutionError: If the dependency cannot be resolved
        """
        if interface in self._singletons:
            return self._singletons[interface]
        
        if interface not in self._registrations:
            raise ResolutionError(f"No registration found for {interface}")
        
        registration = self._registrations[interface]
        implementation = registration['implementation']
        scope = registration['scope']
        
        # Resolve based on scope
        if scope == Scope.SINGLETON:
            # Create singleton instance if not exists
            if interface not in self._singletons:
                instance = self._create_instance(implementation)
                self._singletons[interface] = instance
            return self._singletons[interface]
        elif scope == Scope.TRANSIENT:
            # Create new instance each time
            return self._create_instance(implementation)
        elif scope == Scope.REQUEST:
            # For simplicity, treat as transient in this implementation
            return self._create_instance(implementation)
        else:
            raise ResolutionError(f"Unknown scope: {scope}")
    
    def _create_instance(self, implementation: Union[Type[T], Callable[[], T]]) -> T:
        """
        Create an instance of the implementation.
        
        Args:
            implementation: The implementation type or factory function
            
        Returns:
            The created instance
        """
        try:
            if callable(implementation):
                # If it's a callable, call it directly
                if isinstance(implementation, type):
                    # If it's a type, inspect its constructor parameters
                    return self._inject_dependencies(implementation)  # type: ignore
                else:
                    # If it's a factory function, check for dependencies
                    from .utils import get_injectable_dependencies
                    dependencies = get_injectable_dependencies(implementation)
                    
                    # Resolve dependencies
                    resolved_deps = {}
                    for param_name, dep_type in dependencies.items():
                        resolved_deps[param_name] = self.resolve(dep_type)
                    
                    # Call the factory function with resolved dependencies
                    return implementation(**resolved_deps)  # type: ignore
            else:
                raise ResolutionError(f"Invalid implementation: {implementation}")
        except Exception as e:
            raise ResolutionError(f"Failed to create instance: {e}")
    
    def _inject_dependencies(self, cls: Type[T]) -> T:
        """
        Inject dependencies into a class constructor.
        
        Args:
            cls: The class to instantiate
            
        Returns:
            The instantiated class with dependencies injected
        """
        # Import here to avoid circular imports
        from .utils import get_constructor_parameters
        
        try:
            # Get constructor parameters
            params = get_constructor_parameters(cls)
            
            # Resolve dependencies for each parameter
            dependencies = {}
            for param_name, param_type in params.items():
                # Try to resolve the dependency
                try:
                    dependencies[param_name] = self.resolve(param_type)
                except ResolutionError:
                    # If we can't resolve the dependency, we'll let the class handle it
                    pass
            
            # Instantiate the class with resolved dependencies
            return cls(**dependencies)
        except Exception as e:
            raise ResolutionError(f"Failed to instantiate {cls}: {e}")
    
    def clear(self) -> None:
        """Clear all registrations and singletons."""
        self._registrations.clear()
        self._singletons.clear()