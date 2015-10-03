class Solution(object):
    def binaryTreePaths(self, root):
        treePath = []
        if not root:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        else:
            for path in self.binaryTreePaths(root.left):
                treePath.append(str(root.val) + "->" + path)
            for path in self.binaryTreePaths(root.right):
                treePath.append(str(root.val)+ "->" + path)
        return treePath
        