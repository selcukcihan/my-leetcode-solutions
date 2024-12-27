# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _copy(self, n1, n2):
        while n1:
            n1.val = n2.val
            n1 = n1.next
            n2 = n2.next

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        # 1. safha
        current = head
        counter = 0
        new_list = None
        new_list_current = None
        while counter < left - 1:
            if new_list is None:
                new_list_current = new_list = ListNode(current.val)
            else:
                new_list_current.next = ListNode(current.val)
                new_list_current = new_list_current.next

            current = current.next
            counter += 1

        # 2. safha, ilk bölüm
        stack = []
        # şu an counter == left - 1
        while counter < right:
            stack.append(current.val)
            current = current.next
            counter += 1

        # 2. safha, ikinci bölüm
        while len(stack) > 0:
            val = stack.pop()
            if new_list is None:
                new_list_current = new_list = ListNode(val)
            else:
                new_list_current.next = ListNode(val)
                new_list_current = new_list_current.next

        # 3. safha
        new_list_current.next = current
        self._copy(head, new_list)
        return head


def _print(head):
    while head:
        print(head.val)
        head = head.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed = Solution().reverseBetween(head, 2, 4)

_print(head)
_print(reversed)

# head = ListNode(5)
# reversed = Solution().reverseBetween(head, 1, 1)
# _print(head)
# _print(reversed)
