class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max, current = 0, 0

        for num in nums:
            if num == 1:
                current += 1
                if current > max:
                    max = current
            else:
                current = 0
    
        return max