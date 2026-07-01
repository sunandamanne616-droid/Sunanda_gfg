class Solution:
    def getSecondLargest(self, arr):
        # code here
        arr.sort()
        largest=arr[-1]
        for i in range (len(arr)-1,-1,-1):
            if arr[i]!=largest:
                return arr[i]
        return -1