import json
import os
from typing import List


class BuyAndSellStocks02:

    def max_profit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_idx = [-1 for _ in range(n)]
        sell_idx = [-1 for _ in range(n)]
        profit = [0 for _ in range(n)]
        buy_idx[0] = 0
        sell_idx[0] = 0
        i = 1
        while(i < n):
            if(buy_idx[i-1] >= 0 and prices[buy_idx[i-1]] > prices[i]):
                buy_idx[i] = i
            if(sell_idx[i-1] >= 0 and prices[sell_idx[i-1]] < prices[i]):
                sell_idx[i] = i
            if(buy_idx[i] < sell_idx[i]):
                profit[i] = prices[buy_idx[i]] - prices[sell_idx[i]]
            i = i + 1
