class JSONParser:
    def __init__(self, text: str):
        self.text = text
        self.index = 0
        self.length = len(text)

    def parse(self):
        value = self.parse_value()
        self.skip_whitespace()
        if self.index != self.length:
            raise ValueError(f"Extra data after valid JSON at index {self.index}")
        return value

    # ---------------- Core ----------------

    def parse_value(self):
        self.skip_whitespace()
        if self.match("null"): return None
        if self.match("true"): return True
        if self.match("false"): return False
        ch = self.peek()
        if ch == '"': return self.parse_string()
        if ch == '{': return self.parse_object()
        if ch == '[': return self.parse_array()
        return self.parse_number()

    def parse_object(self):
        obj = {}
        self.expect('{')
        self.skip_whitespace()
        if self.peek() == '}':
            self.expect('}')
            return obj
        while True:
            key = self.parse_string()
            self.skip_whitespace()
            self.expect(':')
            value = self.parse_value()
            obj[key] = value
            self.skip_whitespace()
            if self.peek() == '}':
                self.expect('}')
                break
            self.expect(',')
        return obj

    def parse_array(self):
        arr = []
        self.expect('[')
        self.skip_whitespace()
        if self.peek() == ']':
            self.expect(']')
            return arr
        while True:
            arr.append(self.parse_value())
            self.skip_whitespace()
            if self.peek() == ']':
                self.expect(']')
                break
            self.expect(',')
        return arr

    def parse_string(self):
        self.expect('"')
        result = ""
        while self.index < self.length:
            ch = self.text[self.index]
            self.index += 1
            if ch == '"':
                return result
            elif ch == '\\':
                esc = self.text[self.index]
                self.index += 1
                escape_dict = {
                    '"': '"', '\\': '\\', '/': '/', 'b': '\b',
                    'f': '\f', 'n': '\n', 'r': '\r', 't': '\t'
                }
                result += escape_dict.get(esc, esc)
            else:
                result += ch
        raise ValueError("Unterminated string")

    def parse_number(self):
        start = self.index
        while self.index < self.length and self.text[self.index] in "-0123456789.eE":
            self.index += 1
        num_str = self.text[start:self.index]
        try:
            if '.' in num_str or 'e' in num_str or 'E' in num_str:
                return float(num_str)
            return int(num_str)
        except ValueError:
            raise ValueError(f"Invalid number at index {start}")

    # ---------------- Helpers ----------------

    def skip_whitespace(self):
        while self.index < self.length and self.text[self.index] in " \t\n\r":
            self.index += 1

    def peek(self):
        return self.text[self.index] if self.index < self.length else None

    def expect(self, ch):
        if self.peek() != ch:
            raise ValueError(f"Expected '{ch}' at index {self.index}")
        self.index += 1

    def match(self, keyword):
        end = self.index + len(keyword)
        if self.text[self.index:end] == keyword:
            self.index = end
            return True
        return False
