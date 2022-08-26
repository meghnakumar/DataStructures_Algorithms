class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        eve,odd=0,0
        
        for i in range(len(nums)-1,-1,-1):
            tempEve=max(odd+nums[i],eve)
            tempOdd = max(eve-nums[i],odd)
            eve,odd=tempEve,tempOdd
        return eve