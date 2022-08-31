class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=0
        dict={}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i]=count
                count+=1
        return False
        