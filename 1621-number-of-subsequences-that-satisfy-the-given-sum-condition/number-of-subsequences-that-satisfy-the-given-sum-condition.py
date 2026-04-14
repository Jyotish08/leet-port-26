class Solution(object):
    def numSubseq(self, nums, target):
        mod = 10**9 + 7
        nums.sort()
        
        left, right = 0, len(nums) - 1
        count = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                count += pow(2, right - left, mod)
                count %= mod
                left += 1
            else:
                right -= 1

        return count