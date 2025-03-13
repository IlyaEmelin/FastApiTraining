from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val}{', ' + str(self.next) if self.next else ''}'

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            current_node, next_node = head, head.next
            while True:
                if current_node.val == next_node.val:
                    next_node = next_node.next
                    if next_node is None:
                        current_node.next = None
                        break
                else:
                    current_node.next, current_node, next_node = next_node, next_node, next_node.next
                    if next_node is None:
                        break
        return head


if __name__ == '__main__':
    print('test1:', Solution().deleteDuplicates(
        ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3, None)))))
    ))