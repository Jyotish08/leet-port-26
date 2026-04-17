class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        ispr = [True] * n
        ispr[0] = ispr[1] = False

        i = 2
        while i * i < n:
            if ispr[i]:
                for j in range(i * i, n, i):  # FIX: n instead of n+1
                    ispr[j] = False
            i += 1

        return sum(ispr)