"""
Advanced tests for JSON parser including edge cases and complex scenarios.
"""

import unittest
from json_parser.parser import JSONParser
from json_parser.serializer import JSONSerializer
from json_parser.tokenizer import JSONTokenizer, TokenType
from json_parser.errors import JSONSyntaxError


class TestAdvancedJSONParsing(unittest.TestCase):
    """Test advanced JSON parsing functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = JSONParser('')
        self.serializer = JSONSerializer()
        self.tokenizer = JSONTokenizer('')
    
    def test_parse_string_with_escapes(self):
        """Test parsing strings with escape sequences."""
        # Test common escape sequences
        json_text = '"Hello\\nWorld\\t\\"quoted\\"\\\\backslash"'
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        
        expected = 'Hello\nWorld\t"quoted"\\backslash'
        self.assertEqual(result, expected)
    
    def test_parse_unicode_escapes(self):
        """Test parsing unicode escape sequences."""
        json_text = '"\\u0048\\u0065\\u006C\\u006C\\u006F"'  # "Hello"
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        
        expected = 'Hello'
        self.assertEqual(result, expected)
    
    def test_parse_scientific_notation(self):
        """Test parsing numbers in scientific notation."""
        # Test positive exponent
        json_text = '1.23e4'
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        self.assertEqual(result, 12300.0)
        
        # Test negative exponent
        json_text = '5.67e-2'
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        self.assertEqual(result, 0.0567)
        
        # Test positive number with positive exponent
        json_text = '+1.23E+4'
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        self.assertEqual(result, 12300.0)
    
    def test_parse_complex_nested_structure(self):
        """Test parsing a complex nested structure."""
        json_text = '''
        {
            "menu": {
                "id": "file",
                "value": "File",
                "popup": {
                    "menuitem": [
                        {"value": "New", "onclick": "CreateNewDoc()"},
                        {"value": "Open", "onclick": "OpenDoc()"},
                        {"value": "Close", "onclick": "CloseDoc()"}
                    ]
                }
            }
        }
        '''
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        
        self.assertIsInstance(result, dict)
        self.assertIn("menu", result)
        self.assertIn("popup", result["menu"])
        self.assertIn("menuitem", result["menu"]["popup"])
        self.assertEqual(len(result["menu"]["popup"]["menuitem"]), 3)
    
    def test_tokenize_basic_tokens(self):
        """Test tokenizer produces correct basic tokens."""
        json_text = '{"key": "value", "number": 123}'
        self.tokenizer = JSONTokenizer(json_text)
        tokens = list(self.tokenizer.tokenize())
        
        # Check we have the expected tokens (including EOF)
        self.assertEqual(len(tokens), 10)  # {, "key", :, "value", ,, "number", :, 123, EOF
        
        # Check specific tokens
        self.assertEqual(tokens[0].type, TokenType.LEFT_BRACE)
        self.assertEqual(tokens[1].type, TokenType.STRING)
        self.assertEqual(tokens[1].value, "key")
        self.assertEqual(tokens[2].type, TokenType.COLON)
        self.assertEqual(tokens[3].type, TokenType.STRING)
        self.assertEqual(tokens[3].value, "value")
        self.assertEqual(tokens[4].type, TokenType.COMMA)
        self.assertEqual(tokens[5].type, TokenType.STRING)
        self.assertEqual(tokens[5].value, "number")
        self.assertEqual(tokens[6].type, TokenType.COLON)
        self.assertEqual(tokens[7].type, TokenType.NUMBER)
        self.assertEqual(tokens[7].value, 123)
        self.assertEqual(tokens[8].type, TokenType.EOF)
    
    def test_serialize_with_indentation(self):
        """Test serializing with indentation."""
        data = {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "New York"
            },
            "hobbies": ["reading", "swimming"]
        }
        
        # Test with indentation
        result = self.serializer.serialize(data, indent=2)
        self.assertIn("\n", result)
        self.assertIn("  ", result)  # Check for indentation
        
        # Parse it back to verify it's valid JSON
        parser = JSONParser(result)
        parsed = parser.parse()
        self.assertEqual(parsed, data)


if __name__ == '__main__':
    unittest.main()