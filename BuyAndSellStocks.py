import json
import os
from typing import List


class BuyAndSellStocks:

    max_profit_arr = []
    start_arr = []
    end_arr = []

    def max_profit(self, prices: List[int]) -> int:
        # buy_sell_mat = BuyAndSellStocks.get_buy_sell_matrix(self, prices)
        n = len(prices)
        BuyAndSellStocks.max_profit_arr = [-1 for _ in range(n)]
        BuyAndSellStocks.start_arr = [-1 for _ in range(n)]
        BuyAndSellStocks.end_arr = [-1 for _ in range(n)]
        profit, start, end = BuyAndSellStocks.get_max_profit(
            self, prices, n-1)
        # for i in range(n):
        #     profit = max(profit, BuyAndSellStocks.max_profit_in_num_trade(
        #         self, prices, i))
        # print(profit, start, end)
        return profit

    def get_buy_sell_matrix(self, prices: List[int]) -> List[int]:
        n = len(prices)
        buy_sell_mat = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                buy_sell_mat[i][j] = max(0, prices[j]-prices[i])
        return buy_sell_mat

    def get_max_profit(self, prices: List[int], end: int) -> (int, int, int):

        if(end == 0):
            BuyAndSellStocks.max_profit_arr[end] = 0
            BuyAndSellStocks.start_arr[end] = 0
            BuyAndSellStocks.end_arr[end] = 0

        if(BuyAndSellStocks.max_profit_arr[end] >= 0):
            return (BuyAndSellStocks.max_profit_arr[end], BuyAndSellStocks.start_arr[end],
                    BuyAndSellStocks.end_arr[end])

        prev_max, prev_start, prev_end = BuyAndSellStocks.get_max_profit(
            self, prices, end-1)
        curr_max = 0
        curr_start_idx = end

        for i in range(end):
            price_diff = prices[end] - prices[i]
            # print(i, end, price_diff)
            if(price_diff > curr_max):
                curr_start_idx = i
                curr_max = price_diff
        if(prev_max > curr_max):
            return (prev_max, prev_start, prev_end)
        else:
            return (curr_max, curr_start_idx, end)

    def max_profit_in_num_trade(self, prices: List[int], end: int, num_trades=2) -> int:
        #BuyAndSellStocks.max_profit_arr[end], BuyAndSellStocks.start_arr[end], BuyAndSellStocks.end_arr[end]
        return 0


ans = BuyAndSellStocks()
print(ans.max_profit([1, 2, 4, 3, 9]))
