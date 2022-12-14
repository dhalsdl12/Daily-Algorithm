class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        if len(nums) != 1:
            dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[:i - 1]) + nums[i]

        return max(dp)