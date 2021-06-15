# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepthN(self, root: TreeNode, depth: int) -> int:
        
        if not root.left and not root.right:
            return depth+1
    
        if root.left and root.right:
            
            left = self.minDepthN(root.left, depth+1)
            right = self.minDepthN(root.right, depth+1)
        
            if left < right:
                return left
        
            return right
    
        if root.left:
            return self.minDepthN(root.left, depth+1)
        if root.right:
            return self.minDepthN(root.right, depth+1)
    
        
    
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        
        if root.left and root.right:
            left = self.minDepthN(root.left, 1)
            right = self.minDepthN(root.right, 1)
            
            if left < right:
                return left
            
            return right
            
        if root.left:
            return self.minDepthN(root.left, 1)
            
        if root.right:
            return self.minDepthN(root.right, 1)
        
