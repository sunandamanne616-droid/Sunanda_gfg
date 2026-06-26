class Solution:
    def isPalindrome(self, n):
        og = abs(n)
        reverse = 0
        n = abs(n)

        while n > 0:
            rev = n % 10
            reverse = reverse * 10 + rev
            n //= 10

        return reverse == og