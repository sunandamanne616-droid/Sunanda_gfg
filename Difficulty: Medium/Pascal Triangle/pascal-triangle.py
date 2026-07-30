class Solution:
    def nthRowOfPascalTriangle(self, n):
        ans = []

        def ncr(n, r):
            res = 1
            for i in range(r):
                res = res * (n - i)
                res = res // (i + 1)
            return res

        for c in range(n):
            ans.append(ncr(n - 1, c))

        return ans