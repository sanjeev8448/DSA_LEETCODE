# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev,curr = None,head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
s = Solution()
Node_1 = ListNode(1)
Node_2 = ListNode(2)
Node_3 = ListNode(3)
Node_4 = ListNode(4)
Node_5 = ListNode(5)


Node_1.next = Node_2
Node_2.next = Node_3
Node_3.next = Node_4
Node_4.next = Node_5

a = s.reverseList(Node_1)

while (a != None):
    print(a.val)
    a = a.next


