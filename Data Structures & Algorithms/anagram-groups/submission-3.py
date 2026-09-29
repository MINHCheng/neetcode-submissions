class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = ["".join(sorted(s)) for s in strs]
        
        d : dict = {}

        for s in range(len(strs)):
            if sort[s] in d:
                d[sort[s]].append(strs[s])
            else:
                d[sort[s]] = [strs[s]]
        
        return list(d.values())
        