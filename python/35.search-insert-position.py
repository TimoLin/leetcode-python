#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if (nums[0]>target):
            return 0
        for i in range(1,n):
            if (nums[i] == target):
                return i
            if ( target > nums[i-1] and target< nums[i] ):
                return i

