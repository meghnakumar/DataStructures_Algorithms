class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        value=[float("inf") for i in range(amount+1)]
        value[0] = 0
        for coin in coins:
            for amount in range(len(value)):
                if coin<=amount:
                    value[amount] = min(value[amount], 1+value[amount-coin])
        return value[amount] if value[amount]!=float("inf") else -1
                    
      