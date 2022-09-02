class Solution(object):
    def twoSum(self, nums, target):
        numDict = {}
        for i in range(len(nums)):
            num = nums[i]
            if target-num in numDict:
                return [i,numDict[target-num]]
            numDict[num] = i