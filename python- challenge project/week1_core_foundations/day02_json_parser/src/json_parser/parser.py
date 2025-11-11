"""
Recursive descent parser for JSON.
"""

from typing import Union, List, Dict, Any, Optional
from .tokenizer import JSONTokenizer, Token, TokenType
from .errors import JSONSyntaxError, JSONParseError


class JSONParser:
    """
    Recursive descent parser for JSON.
    
    Implements a parser that converts JSON text into Python data structures
    using a recursive descent parsing approach.
    """
    
    def __init__(self, text: str):
        """
        Initialize the JSON parser with JSON text.
        
        Args:
            text (str): JSON text to parse
        """
        self.tokenizer = JSONTokenizer(text)
        self.tokens = list(self.tokenizer.tokenize())
        self.position = 0
    
    def parse(self) -> Union[Dict, List, str, int, float, bool, None]:
        """
        Parse the JSON text and return the corresponding Python object.
        
        Returns:
            The parsed Python object (dict, list, str, int, float, bool, or None)
            
        Raises:
            JSONSyntaxError: If the JSON text is syntactically invalid
            JSONParseError: If there's an error during parsing
        """
        result = self._parse_value()
        
        # Check for trailing tokens
        if self._current_token().type != TokenType.EOF:
            raise JSONSyntaxError(f"Unexpected token after valid JSON at position {self._current_token().position}")
        
        return result
    
    def _current_token(self) -> Token:
        """Get the current token."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        # Return EOF token if we've consumed all tokens
        return Token(TokenType.EOF, None, len(self.tokens) if self.tokens else 0)
    
    def _peek_token(self) -> TokenType:
        """Peek at the type of the current token."""
        return self._current_token().type
    
    def _consume_token(self) -> Token:
        """Consume and return the current token, advancing to the next."""
        token = self._current_token()
        self.position += 1
        return token
    
    def _expect_token(self, expected_type: TokenType) -> Token:
        """
        Expect a specific token type and consume it.
        
        Args:
            expected_type (TokenType): The expected token type
            
        Returns:
            The consumed token
            
        Raises:
            JSONSyntaxError: If the current token doesn't match the expected type
        """
        token = self._current_token()
        if token.type != expected_type:
            raise JSONSyntaxError(
                f"Expected {expected_type.value}, got {token.type.value} at position {token.position}"
            )
        return self._consume_token()
    
    def _parse_value(self) -> Union[Dict, List, str, int, float, bool, None]:
        """
        Parse a JSON value.
        
        value := object | array | string | number | true | false | null
        """
        token_type = self._peek_token()
        
        if token_type == TokenType.LEFT_BRACE:
            return self._parse_object()
        elif token_type == TokenType.LEFT_BRACKET:
            return self._parse_array()
        elif token_type == TokenType.STRING:
            token = self._consume_token()
            # Ensure the value is a string
            if isinstance(token.value, str):
                return token.value
            else:
                raise JSONParseError(f"Expected string value, got {type(token.value)}")
        elif token_type == TokenType.NUMBER:
            token = self._consume_token()
            # Ensure the value is a number
            if isinstance(token.value, (int, float)):
                return token.value
            else:
                raise JSONParseError(f"Expected number value, got {type(token.value)}")
        elif token_type == TokenType.TRUE:
            self._consume_token()
            return True
        elif token_type == TokenType.FALSE:
            self._consume_token()
            return False
        elif token_type == TokenType.NULL:
            self._consume_token()
            return None
        else:
            raise JSONSyntaxError(
                f"Unexpected token {token_type.value} at position {self._current_token().position}"
            )
    
    def _parse_object(self) -> Dict[str, Any]:
        """
        Parse a JSON object.
        
        object := '{' '}' | '{' members '}'
        members := member (',' member)*
        member := string ':' value
        """
        self._expect_token(TokenType.LEFT_BRACE)
        
        obj: Dict[str, Any] = {}
        
        # Check for empty object
        if self._peek_token() == TokenType.RIGHT_BRACE:
            self._consume_token()
            return obj
        
        # Parse members
        while True:
            # Parse member (string ':' value)
            key_token = self._expect_token(TokenType.STRING)
            # Type checker needs assurance that value is a string
            key = str(key_token.value) if key_token.value is not None else ""
            
            # Check for duplicate keys
            if key in obj:
                raise JSONSyntaxError(f"Duplicate key '{key}' at position {key_token.position}")
            
            self._expect_token(TokenType.COLON)
            value = self._parse_value()
            obj[key] = value
            
            # Check if we have more members or end of object
            if self._peek_token() == TokenType.RIGHT_BRACE:
                self._consume_token()
                break
            elif self._peek_token() == TokenType.COMMA:
                self._consume_token()
                # Continue to next member
            else:
                raise JSONSyntaxError(
                    f"Expected ',' or '}}', got {self._current_token().type.value} "
                    f"at position {self._current_token().position}"
                )
        
        return obj
    
    def _parse_array(self) -> List[Any]:
        """
        Parse a JSON array.
        
        array := '[' ']' | '[' elements ']'
        elements := value (',' value)*
        """
        self._expect_token(TokenType.LEFT_BRACKET)
        
        arr: List[Any] = []
        
        # Check for empty array
        if self._peek_token() == TokenType.RIGHT_BRACKET:
            self._consume_token()
            return arr
        
        # Parse elements
        while True:
            # Parse value
            value = self._parse_value()
            arr.append(value)
            
            # Check if we have more elements or end of array
            if self._peek_token() == TokenType.RIGHT_BRACKET:
                self._consume_token()
                break
            elif self._peek_token() == TokenType.COMMA:
                self._consume_token()
                # Continue to next element
            else:
                raise JSONSyntaxError(
                    f"Expected ',' or ']', got {self._current_token().type.value} "
                    f"at position {self._current_token().position}"
                )
        
        return arr