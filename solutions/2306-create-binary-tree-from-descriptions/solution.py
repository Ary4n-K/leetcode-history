# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {} 
        
        # This is our notepad where we write down anyone who is a child
        children = set() 
        
        # STEP 1: Process every single instruction in the box
        for parent_val, child_val, is_left in descriptions:
            
            # If the parent piece isn't on our workbench, create it!
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            
            # If the child piece isn't on our workbench, create it!
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            # Connect the two pieces! 
            # We grab them from the workbench and snap them together based on the isLeft rule.
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # Write down the child's name on our notepad
            children.add(child_val)
            
        # STEP 2: Find the Root
        # Look through all the instructions one last time...
        for parent_val, child_val, is_left in descriptions:
            
            # If we find a parent who is NOT on our "children" notepad...
            if parent_val not in children:
                
                # We found the big boss! Hand it back from our workbench.
                return nodes[parent_val]
                
        return None
