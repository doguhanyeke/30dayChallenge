# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next:
            slow = slow.next
            if fast.next.next is None:
                break
            fast = fast.next.next
        return slow


s = Solution()
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
head.next = second
second.next = third
third.next = fourth
fourth.next = None
fifth.next = None
result = s.middleNode(head)
print(result.val)
