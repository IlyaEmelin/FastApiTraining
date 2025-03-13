from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left.val if self.left else None} : {self.val} : {self.right.val if self.right else None}'


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            result, stack, current = [], deque(), root
            while True:
                left = current.left
                if left:
                    current.left = None
                    stack.append(current)
                    current = left
                else:
                    result.append(current.val)
                    right = current.right
                    if right:
                        current = right
                    else:
                        try:
                            current = stack.pop()
                        except IndexError:
                            break
            return result
        return []


if __name__ == '__main__':
    print(
        'test1:',
        Solution().inorderTraversal(
            TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
        )  # [1,3,2]
    )
