# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # cut first half
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2