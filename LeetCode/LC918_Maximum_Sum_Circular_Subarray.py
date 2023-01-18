class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        min_dp = [0 for _ in range(n)]
        min_dp[0] = nums[0]
        max_dp = [0 for i in range(n)]
        max_dp[0] = nums[0]
        
        for i in range(1, n):
            max_dp[i] = max(max_dp[i - 1] + nums[i], nums[i])
        
        for i in range(1, n):
            min_dp[i] = min(min_dp[i - 1] + nums[i], nums[i])

        if min(min_dp) == sum(nums):
            return max(max_dp)

        max_dp = [0 for i in range(n)]
        max_dp[0] = nums[0]
        for i in range(1, n):
            max_dp[i] = max(max_dp[i - 1] + nums[i], nums[i])
        return max(sum(nums) - min(min_dp), max(max_dp))