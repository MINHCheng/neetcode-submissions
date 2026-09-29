class MinStack:

    def __init__(self):
        self.stack = []
        self.minu = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minu = val
        else:
            check = val - self.minu
            self.stack.append(check)
            if check < 0:
                self.minu = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.minu = self.minu - pop
        

    def top(self) -> int:
        if not self.stack:
            return
        
        if self.stack[-1] < 0:
            return self.minu
        else:
            return self.minu + self.stack[-1]

    def getMin(self) -> int:
        return self.minu
        
