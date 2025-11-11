"""
JSON Tokenizer for breaking down JSON text into tokens.
"""

from enum import Enum
from typing import Iterator, Union, Optional
from .errors import JSONSyntaxError


class TokenType(Enum):
    """Enumeration of JSON token types."""
    LEFT_BRACE = "{"        # {
    RIGHT_BRACE = "}"       # }
    LEFT_BRACKET = "["      # [
    RIGHT_BRACKET = "]"     # ]
    COLON = ":"             # :
    COMMA = ","             # ,
    STRING = "STRING"       # "..."
    NUMBER = "NUMBER"       # 123, 123.45, -123, etc.
    TRUE = "true"           # true
    FALSE = "false"         # false
    NULL = "null"           # null
    EOF = "EOF"             # End of file


class Token:
    """Represents a single token from the JSON text."""
    
    def __init__(self, type_: TokenType, value: Union[str, int, float, bool, None], position: int = 0):
        self.type = type_
        self.value = value
        self.position = position
    
    def __repr__(self) -> str:
        return f"Token({self.type}, {self.value!r}, {self.position})"


class JSONTokenizer:
    """Tokenizer for JSON text that breaks it into tokens."""
    
    def __init__(self, text: str):
        self.text = text
        self.position = 0
        self.length = len(text)
    
    def tokenize(self) -> Iterator[Token]:
        """Generate tokens from the JSON text."""
        while self.position < self.length:
            self._skip_whitespace()
            
            if self.position >= self.length:
                break
                
            char = self._peek()
            
            # Handle None case
            if char is None:
                break
                
            # Single character tokens
            if char == '{':
                yield Token(TokenType.LEFT_BRACE, char, self.position)
                self._advance()
            elif char == '}':
                yield Token(TokenType.RIGHT_BRACE, char, self.position)
                self._advance()
            elif char == '[':
                yield Token(TokenType.LEFT_BRACKET, char, self.position)
                self._advance()
            elif char == ']':
                yield Token(TokenType.RIGHT_BRACKET, char, self.position)
                self._advance()
            elif char == ':':
                yield Token(TokenType.COLON, char, self.position)
                self._advance()
            elif char == ',':
                yield Token(TokenType.COMMA, char, self.position)
                self._advance()
            # String
            elif char == '"':
                yield self._read_string()
            # Number
            elif char is not None and (char.isdigit() or char == '-' or (char == '+' and self._is_valid_scientific_notation_start())):
                yield self._read_number()
            # Literals (true, false, null)
            elif char == 't':
                yield self._read_true()
            elif char == 'f':
                yield self._read_false()
            elif char == 'n':
                yield self._read_null()
            else:
                raise JSONSyntaxError(f"Unexpected character '{char}' at position {self.position}")
        
        # End of file token
        yield Token(TokenType.EOF, None, self.position)
    
    def _advance(self) -> Optional[str]:
        """Move to the next character and return it."""
        if self.position < self.length:
            char = self.text[self.position]
            self.position += 1
            return char
        return None
    
    def _peek(self) -> Optional[str]:
        """Look at the current character without advancing."""
        if self.position < self.length:
            return self.text[self.position]
        return None
    
    def _peek_next(self) -> Optional[str]:
        """Look at the next character without advancing."""
        if self.position + 1 < self.length:
            return self.text[self.position + 1]
        return None
    
    def _skip_whitespace(self) -> None:
        """Skip whitespace characters."""
        while self.position < self.length and self.text[self.position] in ' \t\n\r':
            self.position += 1
    
    def _read_string(self) -> Token:
        """Read a string token."""
        start_position = self.position
        self._advance()  # Skip opening quote
        
        result = ""
        while self.position < self.length:
            char = self._advance()
            if char is None:
                raise JSONSyntaxError("Unterminated string")
            
            if char == '"':
                # End of string
                return Token(TokenType.STRING, result, start_position)
            elif char == '\\':
                # Escape sequence
                escaped_char = self._advance()
                if escaped_char is None:
                    raise JSONSyntaxError("Unterminated escape sequence")
                
                escape_map = {
                    '"': '"',
                    '\\': '\\',
                    '/': '/',
                    'b': '\b',
                    'f': '\f',
                    'n': '\n',
                    'r': '\r',
                    't': '\t'
                }
                
                if escaped_char in escape_map:
                    result += escape_map[escaped_char]
                elif escaped_char == 'u':
                    # Unicode escape (4 hex digits)
                    unicode_chars = ""
                    for _ in range(4):
                        hex_char = self._advance()
                        if hex_char is None or not hex_char.isalnum():
                            raise JSONSyntaxError("Invalid unicode escape sequence")
                        unicode_chars += hex_char
                    
                    try:
                        result += chr(int(unicode_chars, 16))
                    except ValueError:
                        raise JSONSyntaxError("Invalid unicode escape sequence")
                else:
                    result += '\\' + escaped_char
            else:
                result += char
        
        raise JSONSyntaxError("Unterminated string")
    
    def _read_number(self) -> Token:
        """Read a number token."""
        start_position = self.position
        start = self.position
        
        # Read integer part
        if self._peek() is not None and self._peek() == '-':
            self._advance()
        
        # Read digits
        if not self._read_digits():
            raise JSONSyntaxError(f"Invalid number at position {start_position}")
        
        # Read optional fractional part
        if self._peek() == '.':
            self._advance()  # Skip '.'
            if not self._read_digits():
                raise JSONSyntaxError(f"Invalid number at position {start_position}")
        
        # Read optional exponent part
        if self._peek() in ('e', 'E'):
            self._advance()  # Skip 'e' or 'E'
            # Read optional sign
            if self._peek() in ('+', '-'):
                self._advance()
            if not self._read_digits():
                raise JSONSyntaxError(f"Invalid number at position {start_position}")
        
        number_str = self.text[start:self.position]
        
        # Try to parse as integer first, then as float
        try:
            if '.' not in number_str and 'e' not in number_str.lower():
                value = int(number_str)
            else:
                value = float(number_str)
        except ValueError:
            raise JSONSyntaxError(f"Invalid number format at position {start_position}")
        
        return Token(TokenType.NUMBER, value, start_position)
    
    def _read_digits(self) -> bool:
        """Read consecutive digits. Returns True if at least one digit was read."""
        start_position = self.position
        while self.position < self.length and self.text[self.position].isdigit():
            self._advance()
        return self.position > start_position
    
    def _read_true(self) -> Token:
        """Read a 'true' literal token."""
        start_position = self.position
        if self._match("true"):
            return Token(TokenType.TRUE, True, start_position)
        raise JSONSyntaxError(f"Invalid literal at position {start_position}")
    
    def _read_false(self) -> Token:
        """Read a 'false' literal token."""
        start_position = self.position
        if self._match("false"):
            return Token(TokenType.FALSE, False, start_position)
        raise JSONSyntaxError(f"Invalid literal at position {start_position}")
    
    def _read_null(self) -> Token:
        """Read a 'null' literal token."""
        start_position = self.position
        if self._match("null"):
            return Token(TokenType.NULL, None, start_position)
        raise JSONSyntaxError(f"Invalid literal at position {start_position}")
    
    def _is_valid_scientific_notation_start(self) -> bool:
        """Check if the current position is a valid start for scientific notation."""
        next_char = self._peek_next()
        return next_char is not None and (next_char.isdigit() or next_char == '.')
    
    def _match(self, expected: str) -> bool:
        """Check if the next characters match the expected string."""
        if self.position + len(expected) <= self.length:
            if self.text[self.position:self.position + len(expected)] == expected:
                self.position += len(expected)
                return True
        return False