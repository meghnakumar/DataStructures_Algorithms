class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subs=[]
        
        for i in nums:
            index=None
            for j in range(len(subs)):
                if subs[j]>=i:
                    index=j
                    subs[index] = i
                    break;
            if index is None:
                subs.append(i)
        return len(subs)
            
                
            
            
        
        