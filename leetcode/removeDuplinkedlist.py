"""

Code
Testcase
Testcase
Test Result
83. Remove Duplicates from Sorted List
Easy
Topics
premium lock icon
Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        # 112
        while current is not None and current.next is not None:
            # print(current.val)
            if current.val == current.next.val:
                # print(current.val,current.next.val)
                current.next = current.next.next
                current = current
            else:
                current = current.next
        return head


def createnode(s,e,st):
    rootnode = None
    node = None
    for i in range(s,e,st):
        # x = random.randint(0,20)
        if(node is not None):
            node.next = ListNode(i)
            node = node.next
        else:
            node = ListNode(i)
            rootnode = node

    return rootnode

# node1 = createnode(1,6,2)
# node2 = createnode(0,5,2)
node1 = ListNode(0)
node2 = ListNode(0)
node3 = ListNode(0)
node4 = ListNode(0)
node5 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def printr(node):
    current_node = node
    while current_node:
        print(current_node.val)
        current_node = current_node.next

# printr(node1)
soln = Solution()
printr(soln.deleteDuplicates(node1))