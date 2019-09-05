#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
# Note: The given array is a sorted array which is easier to do it in-place.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # get how many duplicates of each different num
        if nums == []:
            return 0

        i = 0
        while(i < len(nums)):
            # i: The ith differet number
            # n: The number of duplicates of the ith number
            n = nums.count(nums[i])
            if n > 1:
                for nPop in range(1,n):
                    # The element needs to be popped is always in (i+1)
                    nums.pop(i+1)
            i += 1
        return i
