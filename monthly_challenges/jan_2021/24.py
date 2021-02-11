# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        vals = []
        
        head = curr = ListNode(None)
        
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        
        vals.sort()
        for v in vals:
            new_node = ListNode(v)
            curr.next = new_node
            curr = curr.next
        
        return head.next
