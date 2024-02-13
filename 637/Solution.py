# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
    # dfs
    #     self.dic_values = defaultdict(int)
    #     self.dic_num = defaultdict(int)
    #     self.dfs(root,0)
    #     # sorted_values = sorted(self.dic_values.items(),key = lambda x: x[0])
    #     # sorted_num = sorted(self.dic_num.items(),key = lambda x: x[0])
    #     res = []
    #     for key,val in self.dic_values.items():
    #         res.append(round(float(val)/float(self.dic_num[key]),5))
    #     return res

    # def dfs(self, root, depth):
    #     if not root:
    #         return 
    #     self.dic_values[depth] += root.val
    #     self.dic_num[depth] += 1
    #     self.dfs(root.left,depth+1)
    #     self.dfs(root.right,depth+1)

    # bfs
        queue = deque([(root,0)])
        table = defaultdict(list)
        while queue:
            node, depth = queue.popleft()
            table[depth].append(node.val)
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
        return [round(float(sum(table[i]))/float(len(table[i])),5) for i in range(len(table))]


        