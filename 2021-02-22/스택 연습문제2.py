class stack:
    def __init__(self):
        self.data = []
    def push(self, data):
        self.data.append(data)
    def pop(self):