class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, vi in enumerate(prices):
            for j, vj in enumerate(prices):
                if vj-vi > max_profit and j>i:
                    max_profit = vj-vi
        return max_profit