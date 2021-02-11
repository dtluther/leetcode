# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3601/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        2 4 3 -> 342
        5 6 4 -> 465
        = 807 -> 7 0 8
        
        We are adding up the ones column first, which is the first number we're given.
        1. Add the numbers, and the carry
            Assign carry to 1 or 0 as necessary
        2. Throw the ones digit into a stack, maintain the carry
        3. When run linked list runs out, keep doing the addition to the carry and put in the result stack
        4. build linked list (starting at the tail) from the stack
        """
        
        if not l1 or not l2:
            return None

        result_stack = []
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val >= 10:
                carry = 1 # val // 10 will always be 1 with single digits
                val = val % 10
            else:
                carry = 0
            result_stack.append(val)
            l1 = l1.next
            l2 = l2.next
        
        curr = l1 if l1 else l2
        while curr:
            val = curr.val + carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0
            result_stack.append(val)
            curr = curr.next
        
        if carry:
            result_stack.append(carry)
        
        head = ListNode(result_stack.pop())
        while result_stack:
            new_node = ListNode(result_stack.pop())
            new_node.next = head
            head = new_node
        
        return head
                
