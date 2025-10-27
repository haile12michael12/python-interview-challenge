from parser import JSONParser
from serializer import JSONSerializer

json_text = '''
{
    "user": "Hailemichael",
    "age": 22,
    "languages": ["Python", "React", "Laravel"],
    "active": true,
    "address": { "city": "Addis Ababa", "zip": "1000" },
    "bio": null
}
'''

# Parse JSON → Python
parser = JSONParser(json_text)
data = parser.parse()

print("Parsed Python object:\n", data)

# Serialize Python → JSON
serializer = JSONSerializer()
json_back = serializer.to_json(data)

print("\nRe-serialized JSON string:\n", json_back)
