#Given the root of a complete binary tree, return the number of the nodes in the tree.

#According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

#Design an algorithm that runs in less than O(n) time complexity.

#https://leetcode.com/problems/count-complete-tree-nodes/


Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.nums=0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        
        

        def countN(root: Optional[TreeNode]) -> int:

            if root.left is None and root.right is None:
               self.nums+=0
            elif root.left is None and root.right is not None:
               self.nums+=1
               self.countNodes(root.right)
            elif root.left is not None and root.right is None:
               self.nums+=1
               self.countNodes(root.left)
            else:
               self.nums+=2
               self.countNodes(root.left) + self.countNodes(root.right)
               
            return self.nums+1
        res= countN(root)

        return res
            
