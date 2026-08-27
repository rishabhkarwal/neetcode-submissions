class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        best_buy = float('inf')

        for i in range(len(prices)):
            price = prices[i]
            best_buy = min(best_buy, price)
            profits.append(price - best_buy)

        max_profit = max(profits)
        return max_profit if max_profit > 0 else 0