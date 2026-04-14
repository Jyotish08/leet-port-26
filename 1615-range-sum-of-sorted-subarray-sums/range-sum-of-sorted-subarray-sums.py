class Solution(object):
    def rangeSum(self, nums, n, left, right):
        mod = 10**9 + 7
        arr = []

        for i in range(n):
            for j in range(i, n):
                arr.append(sum(nums[i:j+1]))  # O(n)

        arr.sort()

        return sum(arr[left-1:right]) % mod