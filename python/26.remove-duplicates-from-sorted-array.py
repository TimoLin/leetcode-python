#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
# Note: The given array is a sorted array which is easier to do it in-place.
# Ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
#      This solution is more faster (96ms, 78.07%).
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # get how many duplicates of each different num
        if nums == []:
            return 0

        i = 0
        for j in range(len(nums)):
            if (nums[j] != nums[i]):
                i += 1
                nums[i] = nums[j]
                
        return i+1
