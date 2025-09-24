from typing import Optional
import random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_list_node1 = list1
        current_list_node2 = list2

        new_list_node = None
        root_node = None
        K = 0
        if current_list_node1 is None and current_list_node2 is None:
            return None
        elif current_list_node1 is None and current_list_node2 is not None:
            return list2
        elif current_list_node1 is not None and current_list_node2 is None:
            return list1
        else:
            pass
        while current_list_node1 is not None or  current_list_node2 is not None:
            # if (current_list_node2 is None):
            #     print(new_list_node.val)
            if current_list_node1 is not None and  current_list_node2 is not None:
                if current_list_node1.val < current_list_node2.val:
                    if new_list_node is None:
                        new_list_node = current_list_node1
                        root_node = new_list_node
                    else:
                        new_list_node.next = current_list_node1
                        new_list_node = new_list_node.next
                    current_list_node1 = current_list_node1.next
                else:
                    if new_list_node is None:
                        new_list_node = current_list_node2
                        root_node = new_list_node
                    else:
                        new_list_node.next = current_list_node2
                        new_list_node = new_list_node.next
                    current_list_node2 = current_list_node2.next

            else:
                if current_list_node2 is not  None:
                    new_list_node.next = current_list_node2
                    new_list_node = current_list_node2
                    current_list_node2 = current_list_node2.next

                elif current_list_node1 is not None:
                    new_list_node.next = current_list_node1
                    new_list_node = current_list_node1
                    current_list_node1 = current_list_node1.next
                else:
                    break
        return root_node

def main(mergednode: ListNode):
    # from the second loop both are merged
    current_node = mergednode
    len=0
    while current_node:
        # print(current_node.val)
        len+=1
        current_node = current_node.next
    mid= len//2



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




def printr(node):
    current_node = node
    while current_node:
        print(current_node.val)
        current_node = current_node.next

# node1 = createnode(1,6,2)
# node2 = createnode(0,5,2)
# printr(node1)
# printr(node2)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3


node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

mergednode = Solution().mergeTwoLists(node1,node2)

printr(mergednode)

def mergeSort(arr):
    n = len(arr)
    if(n==1):
        return arr
    mid = n//2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    left = mergeSort(leftHalf)
    right = mergeSort(rightHalf)

    result = []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


