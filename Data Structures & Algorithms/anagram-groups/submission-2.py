class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for anagram in strs:
            sorted_anagram = ''.join(sorted(anagram))
            if sorted_anagram not in anagrams_dict:
                anagrams_dict[sorted_anagram] = []
            anagrams_dict[sorted_anagram].append(anagram)
        return list(anagrams_dict.values())   