#Leetcode question Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    #Time: O(n2)
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

#Optimized solution
    #Time = O(n)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = max(prices[right] - prices[left], profit)
            else:
                left = right
            right = right + 1;
        return profit