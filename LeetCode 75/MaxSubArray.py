#LeetCode Question Link: https://leetcode.com/problems/maximum-subarray/
#Time: O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]
        preSum=0
        for i in range(len(nums)):
            if preSum+nums[i]>nums[i]:
                preSum=preSum+nums[i]
            else:
                preSum=nums[i]
            if preSum>sum:
                sum=preSum
        return sum