# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
 
        def dfs(node)-> Optional[TreeNode]:
            if node == None:
                return None
            
            else:
                if node.val == val:
                    return node
                    
                left = dfs(node.left)
                right = dfs(node.right)
                
                if left:
                    return left
                
                if right:
                    return right
                
                return None

                  
                
            
            
        
        
        return dfs(root)