"""
Basic tests for JSON parser.
"""

import unittest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from json_parser.parser import JSONParser
from json_parser.serializer import JSONSerializer
from json_parser.errors import JSONSyntaxError


class TestBasicJSONParsing(unittest.TestCase):
    """Test basic JSON parsing functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = JSONParser('')
        self.serializer = JSONSerializer()
    
    def test_parse_null(self):
        """Test parsing null value."""
        self.parser = JSONParser('null')
        result = self.parser.parse()
        self.assertIsNone(result)
    
    def test_parse_boolean(self):
        """Test parsing boolean values."""
        # Test true
        self.parser = JSONParser('true')
        result = self.parser.parse()
        self.assertTrue(result)
        
        # Test false
        self.parser = JSONParser('false')
        result = self.parser.parse()
        self.assertFalse(result)
    
    def test_parse_string(self):
        """Test parsing string values."""
        self.parser = JSONParser('"hello world"')
        result = self.parser.parse()
        self.assertEqual(result, 'hello world')
    
    def test_parse_empty_string(self):
        """Test parsing empty string."""
        self.parser = JSONParser('""')
        result = self.parser.parse()
        self.assertEqual(result, '')
    
    def test_parse_number(self):
        """Test parsing number values."""
        # Test integer
        self.parser = JSONParser('123')
        result = self.parser.parse()
        self.assertEqual(result, 123)
        
        # Test negative integer
        self.parser = JSONParser('-456')
        result = self.parser.parse()
        self.assertEqual(result, -456)
        
        # Test float
        self.parser = JSONParser('123.45')
        result = self.parser.parse()
        self.assertEqual(result, 123.45)
        
        # Test negative float
        self.parser = JSONParser('-67.89')
        result = self.parser.parse()
        self.assertEqual(result, -67.89)
    
    def test_parse_empty_object(self):
        """Test parsing empty object."""
        self.parser = JSONParser('{}')
        result = self.parser.parse()
        self.assertEqual(result, {})
    
    def test_parse_empty_array(self):
        """Test parsing empty array."""
        self.parser = JSONParser('[]')
        result = self.parser.parse()
        self.assertEqual(result, [])
    
    def test_serialize_basic_types(self):
        """Test serializing basic types."""
        # Test null
        result = self.serializer.serialize(None)
        self.assertEqual(result, 'null')
        
        # Test boolean
        result = self.serializer.serialize(True)
        self.assertEqual(result, 'true')
        
        result = self.serializer.serialize(False)
        self.assertEqual(result, 'false')
        
        # Test string
        result = self.serializer.serialize('hello')
        self.assertEqual(result, '"hello"')
        
        # Test number
        result = self.serializer.serialize(123)
        self.assertEqual(result, '123')
        
        result = self.serializer.serialize(45.67)
        self.assertEqual(result, '45.67')


if __name__ == '__main__':
    unittest.main()