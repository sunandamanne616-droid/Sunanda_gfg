class Solution:
    def armstrongNumber (self, n):
        # code here 
        dump=n
        lenght=len(str(n))
        arm=0
        while n>0:
            rev=n%10
            arm+=pow(rev,lenght)
            n=n//10
        if (dump==arm):
            return True
        else:
            return False
        