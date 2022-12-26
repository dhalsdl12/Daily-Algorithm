class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp1 = [0 for _ in range(len(prices))]
        dp2 = [0 for _ in range(len(prices))]
        for i in range(1, len(prices)):
            dp1[i] = max(dp1[i - 1] + prices[i] - prices[i - 1], dp2[i - 1])
            dp2[i] = max(dp1[i - 1], dp2[i - 1])

        return max(dp1[-1], dp2[-1])