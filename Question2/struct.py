class Sum:
    def __init__(self, _list, value):
        self._list = _list
        self.val = value

class node:
    def __init__(self, value, status="open"):
        self.val = value
        self.status = status
