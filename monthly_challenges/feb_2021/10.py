# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635/

# The hints helped on this one!

"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        A -> A' -> B -> B' -> C -> C' -> None
        |          |
        C          C
        
        """
        if not head:
            return None
        
        # put new nodes in between
        curr = head
        while curr:
            new_node = Node(curr.val)
            ref = curr.next
            curr.next = new_node
            new_node.next = ref
            curr = ref
        

        curr = head
        result = head.next # head if result will be the node after head
        while curr:
            new_node = curr.next
            if curr.random: # if curr has random, random.next should be the random for our new node
                new_node.random = curr.random.next
            else: # otherwise it's none
                new_node.random = None
            ref = new_node.next # the next curr
            if ref: # if ref exists, there is another new node behind it, and we want to connect the new nodes
                new_node.next = ref.next
            curr = ref
  
        return result

"""
Test cases:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.
"""
