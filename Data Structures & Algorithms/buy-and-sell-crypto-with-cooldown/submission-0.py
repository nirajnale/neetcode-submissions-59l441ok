class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        n = len(prices)

        hold = -prices[0]   # holding stock
        sold = 0            # just sold
        rest = 0            # cooldown / doing nothing

        for i in range(1, n):
            prev_sold = sold

            sold = hold + prices[i]
            hold = max(hold, rest - prices[i])
            rest = max(rest, prev_sold)

        return max(sold, rest)