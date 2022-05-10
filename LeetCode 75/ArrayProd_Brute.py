class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        output=list()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    product=product
                else:
                    product=product*nums[j]
            output.append(product)
            product=1;
        return output