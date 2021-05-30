# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
            ans = 0
            while head:
                ans = (ans << 1) | head.val
                head = head.next
            return ans

l1 = ListNode(1)
l2 = ListNode(0)
l3 = ListNode(1)

l1.next = l2
l2.next = l3

print(Solution().getDecimalValue(l1))
