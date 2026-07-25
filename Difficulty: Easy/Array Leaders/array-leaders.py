class Solution:
    def leaders(self, arr):
        maxa=0
        res=[]
        for i in range(len(arr)-1,-1,-1):
            
            if maxa<=arr[i]:
                res.append(arr[i])
            maxa=max(maxa,arr[i])
        return res[::-1]