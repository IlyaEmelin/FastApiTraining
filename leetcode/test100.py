# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __check(self, p_list, q_list, p, q):
        if p and q:
            p_list.append(p)
            q_list.append(q)
            return True
        elif p is None and q is None:
            return True
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list, q_list = [], []
        if p:
            p_list.append(p)
        if q:
            q_list.append(q)

        while p_list and q_list:
            new_p_list, new_q_list = [], []
            if len(p_list) != len(q_list):
                return False

            for p, q in zip(p_list, q_list):
                if p.val != q.val:
                    return False

                result = self.__check(new_p_list, new_q_list, p.left, q.left)
                if result is False:
                    return False

                result = self.__check(new_p_list, new_q_list, p.right, q.right)
                if result is False:
                    return False

            p_list, q_list = new_p_list, new_q_list

        return True
