class Node:
    def __init__(self, Value):
        self.value = Value
        self.Next = None
    
    def __str__(self):
        return str(self.Value)