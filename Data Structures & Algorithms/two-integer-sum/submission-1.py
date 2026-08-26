class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = set()
        nums_set = set(nums)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_set:
                j = nums.index(complement)
                if i < j: return [i, j]
                if j < i: return [j, i]
            else: complements.add(complement)
        
        return []