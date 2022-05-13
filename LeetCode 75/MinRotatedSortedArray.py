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

    #Optimized solution
    def findMin_Optimized(self, nums):
        n = len(nums)
        l = 0
        r = 1
        while r < n:
            if nums[l] < nums[r]:
                l = r
                r = l + 1
            else:
                return nums[r]
        return nums[0]

