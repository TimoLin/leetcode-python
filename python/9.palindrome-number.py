#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
# Note1: Try not to convert the integer to a string
#       return(str(x) == str(x)[::-1])
# Note2: Also reverting the number is not recommended since the result may overflow
# Ref: https://leetcode.com/problems/palindrome-number/solution/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x%10 == 0 and x !=0)):
            return(False)

        half_reverse = 0
        while (x > half_reverse ):
           half_reverse = half_reverse*10+x%10
           x = int(x/10)

        return((half_reverse == x) or (int(half_reverse/10) == x))



