class Solution:
    def removeDuplicates(self, arr):
        if len(arr) == 0:
            return []

        i = 1

        for j in range(1, len(arr)):
            if arr[j] != arr[j - 1]:
                arr[i] = arr[j]
                i += 1

        return arr[:i]
