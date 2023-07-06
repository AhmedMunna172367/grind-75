class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cur_profit = prices[0]
        max_profit = 0
        last = prices[0]
        for p in prices:
            cur_profit += p - last
            cur_profit = max(cur_profit, 0)
            max_profit = max(max_profit, cur_profit)

        return max_profit
