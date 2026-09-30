class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maximum = 0
        while r <= len(prices) - 1:
            if prices[r] < prices[l]:
                l = r
            maximum = max(maximum, prices[r] - prices [l])
            r += 1
        return maximum