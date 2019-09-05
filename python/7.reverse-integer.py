#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
# Note: The given integer is already 32-bit and you just need to check whether the reversed number overflows or not.
class Solution:
    def reverse(self, x: int) -> int:

        if (x>0):
            result = int(str(x)[::-1])
        else:
            result = -int(str(abs(x))[::-1])
            
        if (result > 2147483647 or result < -2147483648):
            return(0)
        else:
            return(result)

