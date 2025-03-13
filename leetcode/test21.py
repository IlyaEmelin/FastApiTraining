from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + (' ' + str(self.next)) if self.next else ''


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        result = ListNode()
        temp, num1, num2 = result, list1.val, list2.val

        while True:
            if num1 is None or (num2 is not None and num1 >= num2):
                temp.val = num2
                list2 = list2.next
            elif num2 is None or (num1 is not None and num2 >= num1):
                temp.val = num1
                list1 = list1.next

            num1, num2 = list1.val if list1 else None, list2.val if list2 else None

            if num1 is None and num2 is None:
                break

            temp.next = ListNode()
            temp = temp.next

        return result


if __name__ == '__main__':
    # [1, 2, 4]
    # [1, 3, 4]
    list_node0 = ListNode(1, ListNode(2, ListNode(4, None)))
    list_node1 = ListNode(1, ListNode(3, ListNode(4, None)))

    print('test1:', Solution().mergeTwoLists(list_node0, list_node1))
