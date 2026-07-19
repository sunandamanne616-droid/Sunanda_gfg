class Solution:
    def removeDuplicates(self, arr):
        j=0
        for i in range(1,len(arr)):
            if arr[i]!=arr[j]:
                j+=1
                arr[j]=arr[i]
        return arr[:j+1]
