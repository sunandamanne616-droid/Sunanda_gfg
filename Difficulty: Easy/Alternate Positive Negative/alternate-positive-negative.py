class Solution:
    def rearrange(self, arr):
        pos_arr = []
        neg_arr = []

        for x in arr:
            if x >= 0:      # 0 is positive
                pos_arr.append(x)
            else:
                neg_arr.append(x)

        pos = 0
        neg = 0
        i = 0

        while pos < len(pos_arr) and neg < len(neg_arr):
            arr[i] = pos_arr[pos]
            i += 1
            pos += 1

            arr[i] = neg_arr[neg]
            i += 1
            neg += 1

        while pos < len(pos_arr):
            arr[i] = pos_arr[pos]
            i += 1
            pos += 1

        while neg < len(neg_arr):
            arr[i] = neg_arr[neg]
            i += 1
            neg += 1

        return arr