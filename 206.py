# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if (head is None):
            return head
        stack = []
        while (head.next is not None):
            stack.append(head)
            head = head.next
        point = head
        while (stack != []):
            point.next = stack.pop()
            point = point.next
        point.next = None
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
