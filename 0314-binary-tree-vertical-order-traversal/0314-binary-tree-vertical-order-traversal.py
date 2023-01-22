# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        column_table = collections.defaultdict(list)
        queue = deque([(root,0)])
        min_column = max_column = 0
        
        while queue:
            node,column = queue.popleft()
            if node is not None:
                min_column = min(min_column,column)
                max_column = max(max_column,column)
            
                column_table[column].append(node.val)
                queue.append((node.left,column - 1))
                queue.append((node.right,column + 1))
                
        return [column_table[x]for x in range(min_column,max_column + 1)]
            