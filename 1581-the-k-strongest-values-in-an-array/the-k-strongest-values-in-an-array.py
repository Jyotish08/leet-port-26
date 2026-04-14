class Solution(object):
    def getStrongest(self, arr, k):
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]

        # Sort by strength
        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)

        return arr[:k]