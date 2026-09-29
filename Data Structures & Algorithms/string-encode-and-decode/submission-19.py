class Solution:

    def encode(self, strs: List[str]) -> str:
        ret : str = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret, i = [], 0
        
        while(i < len(s)):
            j = i
            while(s[j] != '#'):
                j+=1
            
            size = int(s[i:j])

            ret.append(s[j+1 : j + 1 + size])
            i = j+1+size
        return ret
