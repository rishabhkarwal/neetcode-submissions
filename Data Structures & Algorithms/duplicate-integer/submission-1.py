class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # a set of all current seen ones
        for n in nums: # loop through each
            if n in seen: return True # fast-fail: if it's been seen before
            else:         seen.add(n) # else: add it to the set
        return False # haven't seen any duplicates

'''
Time:  O(n)
Space: O(n)
'''