class Item:
    def __init__(self, key, value):
        self._key = key
        self._value = value

    def get_key(self):
        return self._key
    
    def set_key(self, key):
        self._key = key

    def get_value(self):
        return self._value
    
    def set_value(self, value):
        self._value = value
