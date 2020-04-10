import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        self.min_so_far = sys.maxsize

    def push(self, x: int) -> None:
        if len(self.lst) == 0:
            self.lst.append((x, x))
        else:
            top_ele = self.top_both()
            if x < top_ele[1]:
                self.lst.append((x, x))
            else:
                self.lst.append((x, top_ele[1]))

    def pop(self) -> None:
        self.lst.pop()

    def top_both(self):
        return self.lst[-1]

    def top(self) -> int:
        return self.lst[-1][0]

    def getMin(self) -> int:
        return self.top_both()[1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
res = minStack.getMin()   # Returns -3.
print(res)
minStack.push(-5)
minStack.push(-12)
minStack.pop()
res = minStack.top()      # Returns 0.
print(res)
minStack.push(-10)
minStack.push(-4)
minStack.push(0)
minStack.push(-3)
res = minStack.getMin()   # Returns -2.
print(res)
