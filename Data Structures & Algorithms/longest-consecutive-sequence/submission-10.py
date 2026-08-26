class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1: return 1
        best = 0
        count = 1
        nums.sort()
        for i in range(1, len_nums):
            difference = nums[i] - nums[i - 1]
            if difference == 1: count += 1
            elif difference == 0: pass
            else: count = 1
            
            if count > best: best = count
        return best