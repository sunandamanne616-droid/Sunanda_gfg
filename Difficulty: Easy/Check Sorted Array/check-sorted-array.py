class Solution:
    def isSorted(self, arr):
        # code here
        flag=True
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                flag=f=False
                break
        return flag