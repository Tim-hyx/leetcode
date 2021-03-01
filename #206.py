# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 遍历
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

# 递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(cur, prev):
            if cur == None:
                return prev
            res = reverse(cur.next, cur)
            cur.next = prev
            return res
        return reverse(head, None)
