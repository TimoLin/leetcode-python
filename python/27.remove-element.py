#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (nums==[]):
            return 0
        i = 0
        for j in range(len(nums)):
            if (nums[j] != val):
                nums[i] = nums[j]
                i += 1
        return i     
        

