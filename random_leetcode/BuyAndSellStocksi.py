import json
import os
from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class BuyAndSellStocksi:

    def max_profit(self, prices: List[int], start_idx: int, end_idx: int) -> int:
        if(len(prices) == 0):
            return 0
        min_price = prices[start_idx]
        max_profit = float('-inf')
        for i in range(start_idx, end_idx+1):
            if(prices[i] <= min_price):
                min_price = prices[i]
            if(prices[i]-min_price > max_profit):
                max_profit = prices[i]-min_price
        return max_profit


ans = BuyAndSellStocksi()
prices = [1, 2, 5, 4, 3, 1, 2, 6]
print(ans.max_profit(prices, 0, len(prices)-1))
