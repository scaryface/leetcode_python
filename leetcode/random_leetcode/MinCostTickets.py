import json
import os
from typing import List

''' 
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3436/

'''

class MinCostTickets:
    
    def min_cost_tickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        travel_cost = [0 for i in range(days[-1]+1)]
        for i in range(len(travel_cost)):
            if(i not in travel_days):
                travel_cost[i] = travel_cost[i-1]
            else:
                travel_cost[i] = min(travel_cost[max(0, i-1)] + costs[0], min(travel_cost[max(0, i-7)] + costs[1], travel_cost[max(i-30, 0)] + + costs[2]))
        return travel_cost[-1]

f = open(os.getcwd() + "/test_cases/test_cases.json")           
all_data = json.load(f)
test_data = all_data["MinCostTickets"]
ans_obj = MinCostTickets()
for test in test_data:
    ans_test = ans_obj.min_cost_tickets(test_data[test]["input"][0], test_data[test]["input"][1])
    print(ans_test, test_data[test]["output"])
