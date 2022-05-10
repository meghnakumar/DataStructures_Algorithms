#LeetCode Ques Link: https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf_Brute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time = O(n2)
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

    def productExceptSelf_timeOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Time = O(n)
        product = 1
        output = [1] * len(nums)
        rightProduct = [1] * len(nums)
        leftProduct = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                product = product * nums[i - 1]
            leftProduct[i] = product
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != (len(nums) - 1):
                product = product * nums[i + 1]
            rightProduct[i] = product
        for i in range(len(nums)):
            output[i] = (leftProduct[i] * rightProduct[i])
        return output

    def productExceptSelf_spaceOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Removed the result for loop, and made the changes to the output list itself
        product = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                product = product * nums[i - 1]
            output[i] = product
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != (len(nums) - 1):
                product = product * nums[i + 1]
            output[i] = output[i] * product
        return output


