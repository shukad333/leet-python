from linkedlist.LinkedList import LinkedList


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 

From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 

There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        pA = headA
        pB = headB

        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA


sol = Solution()
node1 = LinkedList(4)
node1.next = LinkedList(1)
node1.next.next = LinkedList(8)
node1.next.next.next = LinkedList(4)
node1.next.next.next.next = LinkedList(5)


node2 = LinkedList(5)
node2.next = LinkedList(0)
node2.next.next = LinkedList(1)
node2.next.next.next = LinkedList(8)
node2.next.next.next.next = LinkedList(4)
node2.next.next.next.next.next = LinkedList(5)

print(sol.getIntersectionNode(node1,node2))
