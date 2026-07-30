class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            for j in range(i, len(numbers)):
                if target - numbers[i] == numbers[j]:
                    return[i + 1, j + 1]
        
        return []