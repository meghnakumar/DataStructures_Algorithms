#Leetcode question link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

#Time- O(n)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        n = len(nums)
        for i in nums:
            if i < res:
                res = i
        return res
