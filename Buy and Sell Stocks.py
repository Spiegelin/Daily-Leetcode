# 1.) Is this price cheaper than any other price I've seen before?
# 2.) If I subtract current price by the cheapest price I've found, does this yield 
#     a greater profit than what I've seen so far?

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cheapest = prices[0]

        for current in prices:
            if (current < cheapest):
                cheapest = current
            if (current - cheapest > maxProfit):
                maxProfit = current - cheapest

        return maxProfit


# Toooooo slow
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i,n):
                current = prices[j] - prices[i]
                if (maxProfit < current):
                    maxProfit = current

        return maxProfit