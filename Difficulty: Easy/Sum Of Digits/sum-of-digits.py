class Solution:
    def sumOfDigits(self, n):
        # code here
        lenght=len(str(n))
        count=0
        for i in range(0,lenght):
            temp=n%10
            count+=temp
            n=n//10
        return count