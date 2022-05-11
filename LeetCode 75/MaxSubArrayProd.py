#Leetcode question link: https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        prod = max(nums)
        maxProd = 1
        minProd = 1
        for n in nums:
            if n == 0:
                maxProd, minProd = 1, 1
                continue
            temp = maxProd * n
            maxProd = max(n * maxProd, n * minProd, n)
            minProd = min(temp, n * minProd, n)
            prod = max(prod, maxProd)
        return prod
