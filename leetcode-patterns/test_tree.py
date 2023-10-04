from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 543. Diameter of Binary Tree
class Solution543:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = float("-inf")

        def max_depth(node):
            if not node:
                return 0

            left, right = max_depth(node.left), max_depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        max_depth(root)
        return self.diameter


# 110. Balanced Binary Tree
class Solution110:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        def balance(node):
            if not node:
                return True
            return balance(node.left) and balance(node.right) and abs(depth(node.left) - depth(node.right)) <= 1

        return balance(root)


# 572. Subtree of Another Tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def is_same(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return is_same(p.left, q.left) and is_same(p.right, q.right)

        if is_same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# 226. Invert Binary Tree
class Solution226:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# 104. Maximum Depth of Binary Tree
class Solution104:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)


# 100. Same Tree
class Solution100:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


# 235. Lowest Common Ancestor of a Binary Search Tree
class Solution235:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                break
        return root


# 1448. Count Good Nodes in Binary Tree
class Solution1448:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxi):
            if not node:
                return 0

            val = 1 if node.val >= maxi else 0
            maxi = max(maxi, node.val)
            return val + dfs(node.left, maxi) + dfs(node.right, maxi)

        return dfs(root, float("-inf"))


# 199. Binary Tree Right Side View
class Solution199:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        q = deque()
        if root:
            q.append(root)
        res = []
        right_view = None
        while q:
            for _i in range(len(q)):
                node = q.popleft()
                right_view = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(right_view)
        return res


# 102. Binary Tree Level Order Traversal
class Solution102:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        q = deque()
        if root:
            q.append(root)
        res = []
        while q:
            level = []
            for _i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res


# 98. Validate Binary Search Tree
class Solution98:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, node, right):
            if not node:
                return True
            if left < node.val < right:
                return dfs(left, node.left, node.val) and dfs(node.val, node.right, right)
            return False

        return dfs(float("-inf"), root, float("inf"))


# 230. Kth Smallest Element in a BST
class Solution230:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)

        dfs(root)
        return res[k - 1]


# 105. Construct Binary Tree from Preorder and Inorder Traversal
class Solution105:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if preorder and inorder:
            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1 :])
            return root
