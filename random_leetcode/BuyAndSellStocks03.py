import os
import json
from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


class BuyAndSellStocks03:

    max_profit_arr = None
    start_arr = None
    end_arr = None
    max_profit_val = float('-inf')

    def __init__(self, prices: List[int], n: int):
        BuyAndSellStocks03.max_profit_arr = [
            [float('-inf') for _ in range(n)] for _ in range(n)]
        BuyAndSellStocks03.start_arr = [
            [prices[0] for _ in range(n)] for _ in range(n)]
        BuyAndSellStocks03.end_arr = [
            [prices[0] for _ in range(n)] for _ in range(n)]


    def __max_profit__(self, prices: List[int]) -> int:
        if(len(prices) == 0):
            return 0
        min_price_idx = prices[0]
        max_profit = float('-inf')
        curr_idx = 0
        while(curr_idx < len(prices)):
            BuyAndSellStocks03.start_arr[0][curr_idx] = min_price_idx
            if(prices[curr_idx]-prices[min_price_idx] > max_profit):
                max_profit = prices[curr_idx]-prices[min_price_idx]
                BuyAndSellStocks03.end_arr[0][curr_idx] = curr_idx
            else:
                BuyAndSellStocks03.end_arr[0][curr_idx] = BuyAndSellStocks03.end_arr[0][curr_idx - 1]
            BuyAndSellStocks03.max_profit_arr[0][curr_idx] = max_profit
            if(prices[curr_idx] < prices[min_price_idx]):
                min_price_idx = curr_idx
            curr_idx = curr_idx + 1
        

    def __set_values__(self, max_profit, start_idx, end_idx, begin, end):
        BuyAndSellStocks03.max_profit_arr[begin][end] = max_profit
        BuyAndSellStocks03.start_arr[begin][end] = start_idx
        BuyAndSellStocks03.end_arr[begin][end] = end_idx

    def __is_profit_valid__(self, begin, end) -> bool:
        if(BuyAndSellStocks03.max_profit_arr[begin][end] > float('-inf')):
            return True
        return False

    def __get_return_val__(self, begin, end) -> (int, int, int):
        return (BuyAndSellStocks03.max_profit_arr[begin][end], 
        BuyAndSellStocks03.start_arr[begin][end], BuyAndSellStocks03.end_arr[begin][end])


    def max_profit(self, prices):
        n = len(prices)
        if(n == 0):
            return 0
        BuyAndSellStocks03.__max_profit__(self, prices)
        for i in range(0, n):
            for j in range(0, n):
                BuyAndSellStocks03.get_max_profit(self, prices, i,j)

    def get_max_profit(self, prices: List[int], start_idx: int, end_idx: int) -> (int, int, int):
        print(start_idx, end_idx)

        if(start_idx == end_idx):
            BuyAndSellStocks03.__set_values__(self, 0,start_idx, end_idx, start_idx, end_idx)
            return (0,start_idx, end_idx)

        if(BuyAndSellStocks03.__is_profit_valid__(self, start_idx, end_idx)):
            return BuyAndSellStocks03.__get_return_val__(self, start_idx, end_idx)

        elif(end_idx < start_idx):
            return BuyAndSellStocks03.__get_return_val__(self, end_idx, start_idx)

        else:

            prev_profit, prev_buy_idx, prev_sell_idx = \
            BuyAndSellStocks03.get_max_profit(self, prices, start_idx-1, end_idx)
            
            if(prev_buy_idx > start_idx-1):
                BuyAndSellStocks03.__set_values__(self, prev_profit, prev_buy_idx, prev_sell_idx, start_idx, end_idx)
                return BuyAndSellStocks03.__get_return_val__(self, start_idx, end_idx)
            
            prev_profit, prev_buy_idx, prev_sell_idx = \
            BuyAndSellStocks03.get_max_profit(self, prices, start_idx, end_idx-1)

            if(prev_sell_idx == end_idx-1):
                if(prices[end_idx] > prices[end_idx-1]):
                    prev_profit = prev_profit + prices[end_idx] - prices[end_idx-1]
                    prev_sell_idx = end_idx
            
            BuyAndSellStocks03.__set_values__(self, prev_profit, prev_buy_idx, prev_sell_idx, start_idx, end_idx)                
            return BuyAndSellStocks03.__get_return_val__(self, start_idx, end_idx)

prices = [1,2,5,4,3,1,2,6]
ans = BuyAndSellStocks03(prices=prices, n=len(prices))
#print(ans.get_max_profit(prices, len(prices)-1, len(prices)-1))
ans.max_profit(prices)
print(ans.max_profit_arr)