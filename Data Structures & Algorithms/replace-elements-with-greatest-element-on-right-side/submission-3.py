class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        maxRight = -1

        for i in range(n-1, -1, -1):
            ans[i] = maxRight
            maxRight = max(maxRight, arr[i])
        
        arr = ans
        return arr