class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.mins = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if self.mins:
            new_min = min(x, self.mins[-1])
        else:
            new_min = x
        self.mins.append(new_min)

    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()

    def top(self) -> int:
        try:
            return self.values[-1]
        except IndexError:
            raise IndexError("Stack is empty")

    def getMin(self) -> int:
        try:
            return self.mins[-1]
        except IndexError:
            raise IndexError("Stack is empty")

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
