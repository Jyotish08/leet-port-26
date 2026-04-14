class Solution(object):
    def rangeSum(self, nums, n, left, right):
        mod = 10**9 + 7
        
        # Build prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        arr = []

        # Generate all subarray sums in O(1) each
        for i in range(n):
            for j in range(i, n):
                arr.append(prefix[j+1] - prefix[i])

        arr.sort()

        return sum(arr[left-1:right]) % mod