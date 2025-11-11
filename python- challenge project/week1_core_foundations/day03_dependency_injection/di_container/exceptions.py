"""
Custom exception classes for Dependency Injection Container.
"""


class DIError(Exception):
    """Base exception for DI container errors."""
    pass


class RegistrationError(DIError):
    """Raised when there's an error during dependency registration."""
    pass


class ResolutionError(DIError):
    """Raised when there's an error during dependency resolution."""
    pass