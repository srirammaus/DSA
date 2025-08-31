from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # here digits are stored inside a listnode , which are in reverse orderof that list exmapple consider this as linked list [2,3,4] then the reverse order digits is 432
        # convert the list of numbers into digit
        main_node = None
        root_node = None
        carry = 0
        while l1 or l2:

            # print(l1.val if l1 else 0  , l2.val if l2 else  0  )
            L1 = l1.val if l1 else 0
            L2 = l2.val if l2 else  0
            total = L1 + L2 + carry

            if total > 9:
                carry = total // 10
                total = total % 10
            else:
                carry = 0

            # print(carry,total)
            if main_node != None:
                newNode = ListNode(total)
                main_node.next = newNode
                main_node = newNode
            else:
                newNode = ListNode(total)
                main_node = newNode
                root_node = newNode
            l1= l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 == None and  l2 == None and carry != 0:
                l1 = ListNode(0)

        return root_node
def nodeCreater(arr):
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)

    # node1.next = node2;
    # node2.next = node3;
    # node3.next = node4;
    # node4.next = node5;
    #
    # current_node =  node1
    # while current_node:
    #     print(current_node.val)
    #     current_node = current_node.next
    # return node1

    node = ListNode(arr[0])
    rootnode = node
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next

    return rootnode
# test = (nodeCreater([2,3,4]))
#
# while test:
#     print(test.val)
#     test = test.next
#

l1= nodeCreater([9,9,9,9,9,9,9])
l2 = nodeCreater([9,9,9,9])

test = Solution().addTwoNumbers(l1, l2)

while test:
    print(test.val)
    test = test.next

