#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
# Note: This solution replace the six instances with single letters 
#       and also a dict is used. String replace operation may cause low effiency.
class Solution:
    def romanToInt(self, s: str) -> int:
        romanLetter = dict([('I',1), ('V',5), ('X',10), ('L',50), ('C',100), ('D',500), ('M',1000),('a',4), ('b',9), ('c',40), ('d',90), ('e',400), ('f',900)])
        # Replace IV->a, IX->b, XL->c, XC->d, CD->e, CM->f
        s = s.replace("IV",'a')
        s = s.replace("IX",'b')
        s = s.replace("XL",'c')
        s = s.replace("XC",'d')
        s = s.replace("CD",'e')
        s = s.replace("CM",'f')

        val = 0
        for symb in s:
            val += romanLetter[symb]

        return(val)
        
