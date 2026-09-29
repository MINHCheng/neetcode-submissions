class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        dict_s : dict = {}
        dict_t : dict = {}

        for s_char, t_char in zip(s, t):
            if s_char in dict_s:
                dict_s[s_char] +=1
            else:
                dict_s[s_char] = 1
            if t_char in dict_t:
                dict_t[t_char] +=1
            else:
                dict_t[t_char] = 1
        if dict_t == dict_s:
            return True
        return False