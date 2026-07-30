class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copynums = set(nums)
        return False if len(copynums) == len(nums) else True