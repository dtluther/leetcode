# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3627/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        
        p1 = head
        p2 = head.next.next
        
        while p1 and p2:
            if p1 == p2:
                return True
            p1 = p1.next
            if not p2.next or not p2.next.next:
                return False
            p2 = p2.next.next
        
        return False
