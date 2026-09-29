from typing import List
import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b),  # truncate toward 0
        }
        stack = []

        for t in tokens:
            if t in ops:
                b = stack.pop()   # right
                a = stack.pop()   # left
                stack.append(ops[t](a, b))
            else:
                stack.append(int(t))

        return stack[-1]
