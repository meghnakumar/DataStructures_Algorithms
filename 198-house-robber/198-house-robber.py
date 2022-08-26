class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<3:
            return max(nums)
        rob1=rob2=0
        
        #rob1 for n and rob2 for n+1
        for i in nums:
            temp=max(i+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
#         eve=0
#         odd=0
#         yes=0 
#         np=0
        
        
#         for i in range(0,len(nums),2):
#             eve=eve+nums[i]
            
#         for i in range(1,len(nums),2):
#             odd = odd+nums[i]
       
        
            
#         return max(eve,odd,yes,np)
            
        
        