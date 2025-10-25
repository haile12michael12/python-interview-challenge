"""
Challenge 1: Serialize and Deserialize Binary Tree

Problem Description:
Design an algorithm to serialize and deserialize a binary tree. 

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Example:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

Approach:
Use BFS (level-order traversal) for serialization and deserialization.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        Args:
            root (TreeNode): Root of the binary tree
            
        Returns:
            str: Serialized representation of the tree
        """
        # Your implementation here
        pass

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        Args:
            data (str): Serialized representation of the tree
            
        Returns:
            TreeNode: Root of the deserialized binary tree
        """
        # Your implementation here
        pass

# Test cases
if __name__ == "__main__":
    # Helper function to build tree from list for testing
    def build_tree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root
    
    # Helper function to convert tree to list for testing
    def tree_to_list(root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result
    
    # Test case 1
    nodes1 = [1,2,3,None,None,4,5]
    root1 = build_tree(nodes1)
    codec = Codec()
    serialized = codec.serialize(root1)
    print(f"Serialized: {serialized}")
    deserialized = codec.deserialize(serialized)
    print(f"Deserialized: {tree_to_list(deserialized)}")