class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = 0, 1
        maxProfit = 0
        for i in range(len(prices)-1):
            if prices[high] < prices[low]:
                low = high
            if prices[high] - prices[low] > maxProfit:
                maxProfit = prices[high] - prices[low]
            high += 1
        return maxProfit