#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum=0
        index = 0
        node = l1
        while node:
            sum += node.val*pow(10,index)
            node = node.next
            index += 1
        index = 0
        node = l2
        while node:
            sum += node.val*pow(10,index)
            node = node.next
            index += 1

        for i, digit in enumerate(str(sum)[::-1]):
            newNode = ListNode(digit)
            if i == 0:
                newLD = newNode
                node = newLD
            else:
                node.next = newNode
                node = node.next
        return(newLD)

