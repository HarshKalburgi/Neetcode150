# Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self,head):
        length = 0
        while head:
            length+=1
            head = head.next
        return length
    def reverseGroup(self,head,k,length):
        if length<k:
            return head
        curr = head
        prev = None
        next = None
        count = 0
        while curr and count<k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count+=1
        if next:
            head.next = self.reverseGroup(next,k,length-k)
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.getLength(head)
        return self.reverseGroup(head,k,length)



        