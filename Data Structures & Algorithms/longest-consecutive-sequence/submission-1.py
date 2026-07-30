class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        count_max = 1
        count = 1
        for i in range (len(nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                continue
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                count = count + 1
            else:
                count_max = max(count_max, count)
                count = 1
        
        return max(count_max, count)