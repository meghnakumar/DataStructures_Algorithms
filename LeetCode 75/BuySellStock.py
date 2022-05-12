#Leetcode question Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit_bruteForce(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[i] < prices[j]:
                    profit = max(prices[j] - prices[i], profit)

        return profit