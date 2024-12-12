from typing import List

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4] => 5 (6 - 1)
        # [2,1,2,1,0,1,2] => 2 (2 - 0)
        # [3,3,5,0,0,3,1,4] => 4 (4 - 0)
        # keep track of current max profit by keeping track of where you bought and sold as well as the diff
        # at each iteration,
        #   if current value is lower than the buying price, buy from this price
        #   if current value is higher than the selling price, sell from this price instead and update the diff as well
        if len(prices) <= 1:
            return 0
        bought = prices[0]
        sold = None
        max_profit = 0
        for i in range(1, len(prices)):
            p = prices[i]
            # print(f"Iteration {i}: p[i]={p}, sold={sold}, bought={bought}")
            if p < bought:
                bought = p
                sold = None
            else:
                if (sold is None or p >= sold) and p - bought > max_profit:
                    sold = p
                    max_profit = sold - bought
                    # print(f"Making profit {max_profit} from {sold} and {bought}")
        return max_profit


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(Solution().maxProfit([3, 2, 6, 5, 0, 3]))
