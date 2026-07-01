class Solution:
    def largest(self, arr):
        # code here
        largest=-1
        for i in arr:
            if i>largest:
                largest=i
        return largest
        
