class Solution:
    def missingNum(self, arr):
        n=len(arr)+1
        ass=sum(arr)
        summ = (n * (n + 1)) // 2
        return summ-ass