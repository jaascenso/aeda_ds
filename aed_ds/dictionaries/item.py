class Item:
    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key
    
    @property.setter
    def key(self, key):
        self._key = key

    @property
    def value(self):
        return self._value
    
    @property.setter
    def value(self, value):
        self._value = value
