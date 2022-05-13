#LeetCode question link: https://leetcode.com/problems/contains-duplicate/submissions/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = count
                count += 1
        return False
