#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
# Note: Stack data structure is used here.
#       Let "({})" as an example:
#       -(-  #{ is the next to push to the stack
#       -({- #} is the next and it forms a pair with {, so just pop { from the top of the stack
#       -(-  #) is the next and it forms a pair with (, so pop ( from the top of the stack
#       --   #stack is empty, return True, or stack is not empty return False
#            # If a back parentheses is not a pair with the top element of the stack, this means 
#            # it's not a valid expression, return False

class Solution:
    def isValid(self, s: str) -> bool:

        if (s == "" ):
             return True
        
        ptDict = dict([('(',')'), ('{','}'), ('[',']')])
        stack = []
        
        if (len(s)%2 == 1):
            return False
        else:
            for temp in s:
                if stack != [] and temp == ptDict[stack[-1]]:
                    stack.pop(-1)
                else:
                    if temp in ")}]":
                        return False
                    else:
                        stack.append(temp)
                
            if stack == []:
                return True
            else:
                return False

