class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        
        maxRight = -1
        for i in range(len(arr) - 1, -1, -1):
            res[i] = maxRight
            maxRight = max(maxRight, arr[i])

        arr = res
        return arr