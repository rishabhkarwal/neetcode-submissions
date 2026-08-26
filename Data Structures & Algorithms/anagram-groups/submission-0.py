class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [''.join(sorted(s)) for s in strs]
        anagrams = {anagram : [] for anagram in set(sorted_strs)}
        for i in range(len(strs)):
            anagrams[sorted_strs[i]].append(strs[i])
        return list(anagrams.values())