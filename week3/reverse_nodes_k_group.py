# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 1:
            return head
        groupprev = dummy = ListNode()
        dummy.next = head
        while (True):
            start = groupprev.next
            end = groupprev
            for i in range(k):
                end = end.next
                if end is None:
                    return dummy.next
            next_group = end.next
            end.next = None
            # groupprev.next = reverseLinkedList(start)
            prev = None
            curr = start
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            groupprev.next = prev
            start.next = next_group
            groupprev = start

        # dummy = ListNode(0)
        # dummy.next = head
        # prev = dummy
        # while True:
        #     start = prev.next
        #     end = prev
        #     for i in range(k):
        #         end = end.next
        #         if end is None:
        #             return dummy.next
        #     next_group = end.next
        #     end.next = None
        #     prev.next = reverseLinkedList(head)
        #     start.next = next_group
        #     prev = start
                # next_group = end.next
                # end.next = None  # break the group
                # prev.next = reverseLinkedList(start)  # reverse the group
                # start.next = next_group  # reconnect the reversed group
                # prev = start  # move prev to the end of reversed group
