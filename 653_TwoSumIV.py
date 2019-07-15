from Queue import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTargetByNode(self, node, k, dict):

        if(node):
            if node.val in dict.keys():
                self.result = True
            else:
                dict[k - node.val] = True

        if self.result == True:
            return self.result
        else:
            if node.left:
                self.findTargetByNode(node.left, k, dict)
            if node.right:
                self.findTargetByNode(node.right, k,dict)


    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.result = False
        dict = {}
        self.findTargetByNode(root, k, dict)
        return self.result


s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.right = TreeNode(6)
root.right.right = TreeNode(7)

print s.findTarget(root, 9)