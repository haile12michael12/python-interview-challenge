"""
Custom error classes for JSON Parser.
"""


class JSONParseError(Exception):
    """Base exception for JSON parsing errors."""
    pass


class JSONSyntaxError(JSONParseError):
    """Raised when JSON syntax is invalid."""
    pass


class JSONDecodeError(JSONParseError):
    """Raised when JSON cannot be decoded."""
    pass