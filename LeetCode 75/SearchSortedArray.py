#Leetcode Question Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

#Approach - Two while loops
# First loop using binary search to find the pivot around which the rotation has happened (log n)
#Second loop based on the target value and pivot use binary search to get the number(log n)

class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while (l < r):
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        start = l
        l = 0
        r = len(nums) - 1

        if target >= nums[start] and target <= nums[r]:
            l = start
        else:
            r = start

        while (l <= r):
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return -1




