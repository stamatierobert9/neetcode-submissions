class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice = {}

        for i,n in enumerate(nums):
            indice[n] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in indice and indice[diff] != i:
                return [i, indice[diff]]
        
        return []