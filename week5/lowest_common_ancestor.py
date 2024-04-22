# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root
        # stack = [root]
        # parent = {root: None}
        # while p not in parent or q not in parent:
        #     node = stack.pop()
        #     if node.left:
        #         parent[node.left] = node
        #         stack.append(node.left)
        #     if node.right:
        #         parent[node.right] = node
        #         stack.append(node.right)
        # # Ancestors set() for node p.
        # ancestors = set()

        # # Process all ancestors for node p using parent pointers.
        # while p:
        #     ancestors.add(p)
        #     p = parent[p]

        # # The first ancestor of q which appears in
        # # p's ancestor set() is their lowest common ancestor.
        # while q not in ancestors:
        #     q = parent[q]
        # return q