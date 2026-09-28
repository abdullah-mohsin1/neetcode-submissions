class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyLow = 0
        sellHigh = 1
        maxProfit = 0
        while sellHigh < len(prices):
            if prices[sellHigh] < prices[buyLow]:
                buyLow = sellHigh
            elif prices[sellHigh] - prices[buyLow] > maxProfit:
                maxProfit = prices[sellHigh] - prices[buyLow]
            sellHigh += 1
        return maxProfit