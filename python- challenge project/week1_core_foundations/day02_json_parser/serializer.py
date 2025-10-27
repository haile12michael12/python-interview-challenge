import json

class JSONSerializer:
    def to_json(self, obj, indent=None):
        if obj is None:
            return "null"
        if isinstance(obj, bool):
            return "true" if obj else "false"
        if isinstance(obj, (int, float)):
            return str(obj)
        if isinstance(obj, str):
            return '"' + obj.replace('"', '\\"') + '"'
        if isinstance(obj, list):
            return "[" + ", ".join(self.to_json(v, indent) for v in obj) + "]"
        if isinstance(obj, dict):
            items = []
            for k, v in obj.items():
                items.append(self.to_json(str(k)) + ": " + self.to_json(v, indent))
            inner = ", ".join(items)
            return "{" + inner + "}"
        raise TypeError(f"Type {type(obj)} not serializable")
