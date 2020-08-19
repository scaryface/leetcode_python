import json
import os
from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


class BuyAndSellStocksiii:

    def max_profit(self, prices: List[int]) -> int:
        profit = 0
        buy_idx = 0
        sell_idx = 0
        for i in range(len(prices)):
            if(prices[i] > prices[sell_idx]):
                profit = profit + prices[i] - prices[sell_idx]
                sell_idx = i
            elif(prices[i] < prices[sell_idx]):
                buy_idx = i
                if(buy_idx > sell_idx):
                    sell_idx = buy_idx
        return profit


ans = BuyAndSellStocksiii()
prices = [7,1,5,3,6,4]
print(ans.max_profit(prices))
