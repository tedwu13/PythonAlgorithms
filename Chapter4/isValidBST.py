def isValidBST(self, root):
    return self.helper(root, float("-infinity"), float("infinity"))

def helper(self, root, min, max):
    if root == None:
        return True
    elif root.val <= min or root.val >= max:
        return False
    else:
        return self.helper(root.right, root.val, max) and self.helper(root.left, min, root.val)
