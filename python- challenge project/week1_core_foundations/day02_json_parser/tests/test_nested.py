"""
Tests for nested JSON structures.
"""

import unittest
from json_parser.parser import JSONParser
from json_parser.serializer import JSONSerializer
from json_parser.errors import JSONSyntaxError


class TestNestedJSONParsing(unittest.TestCase):
    """Test nested JSON parsing functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = JSONParser('')
        self.serializer = JSONSerializer()
    
    def test_parse_nested_object(self):
        """Test parsing nested objects."""
        json_text = '{"name": "John", "address": {"city": "New York", "zip": "10001"}}'
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        
        expected = {
            "name": "John",
            "address": {
                "city": "New York",
                "zip": "10001"
            }
        }
        
        self.assertEqual(result, expected)
    
    def test_parse_nested_array(self):
        """Test parsing nested arrays."""
        json_text = '[1, [2, 3], [4, [5, 6]]]'
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        
        expected = [1, [2, 3], [4, [5, 6]]]
        self.assertEqual(result, expected)
    
    def test_parse_mixed_nested_structures(self):
        """Test parsing mixed nested structures."""
        json_text = '''
        {
            "users": [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25}
            ],
            "metadata": {
                "total": 2,
                "active": true
            }
        }
        '''
        self.parser = JSONParser(json_text)
        result = self.parser.parse()
        
        expected = {
            "users": [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25}
            ],
            "metadata": {
                "total": 2,
                "active": True
            }
        }
        
        self.assertEqual(result, expected)
    
    def test_serialize_nested_structures(self):
        """Test serializing nested structures."""
        data = {
            "person": {
                "name": "Charlie",
                "hobbies": ["reading", "swimming"],
                "address": {
                    "street": "123 Main St",
                    "coordinates": [40.7128, -74.0060]
                }
            },
            "active": True
        }
        
        result = self.serializer.serialize(data)
        # Parse it back to verify it's valid JSON
        parser = JSONParser(result)
        parsed = parser.parse()
        
        self.assertEqual(parsed, data)


if __name__ == '__main__':
    unittest.main()