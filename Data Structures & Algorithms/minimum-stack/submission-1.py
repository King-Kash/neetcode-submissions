class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        last_item = self.stack[-1]
        self.stack.remove(last_item)
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return min(self.stack)
        
