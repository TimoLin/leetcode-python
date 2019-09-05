#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        data = []

        cur = l1
        while (cur):
            data.append(cur.val)
            cur = cur.next

        cur = l2
        while (cur):
            data.append(cur.val)
            cur = cur.next

        if (data == []):
            return ( ListNode('') )
       
        data.sort()
        
        for n, temp in enumerate(data):
            if n == 0:
                l = ListNode(temp)
                cur = l
            else:
                cur.next = ListNode(temp)
                cur = cur.next
             
            

        return (l)

