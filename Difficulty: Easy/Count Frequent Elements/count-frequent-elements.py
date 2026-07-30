class Solution:
    def countOccurence(self, arr, k):
        n = len(arr)
        limit = n // k
        freq={}
        ans=0
        for nums in arr:
            freq[nums]=freq.get(nums,0)+1
        for k,v in freq.items():
            if v>limit:
                ans+=1
        return ans
            