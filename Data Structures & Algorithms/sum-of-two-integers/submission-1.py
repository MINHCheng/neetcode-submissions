class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        res = 0
        carry = -1
        while carry != 0:
            if carry == -1:
                xor = (a ^ b) & MASK
                carry = ((a & b) << 1) & MASK
            else:
                xor = (carry ^ res) & MASK
                carry = ((res & carry) << 1) & MASK
            res = xor
            
        # Handle negative numbers for Python's arbitrary-precision integers
        return res if res <= MAX_INT else ~(res ^ MASK)


  

                    
        