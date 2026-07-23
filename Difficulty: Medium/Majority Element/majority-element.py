class Solution:
    def majorityElement(self, arr):
        #code here
        maj=len(arr)//2
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for k,v in freq.items():
            if v>maj:
                return k
            
        return -1
            