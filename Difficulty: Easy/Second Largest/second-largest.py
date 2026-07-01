class Solution:
    def getSecondLargest(self, arr):
        first=-1
        sec=-1
        for i in arr:
            if i>first:
                first=i
        for i in arr:
            if i>sec and i!=first:
                sec=i
        return sec
            