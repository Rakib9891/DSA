# Given a binary search tree and a integer target. Return true if the target exists in the tree else return false.

# Input: tree = [20, 12, 23, 5, 13, 21, 27], target = 13
# Output: Found 13!

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def searchNode(root, target):
    res = None
    def dfs(root):
        if not root: return
        nonlocal res

        if target == root.val:
            res = root.val
            return
        dfs(root.left)
        dfs(root.right)
    
    dfs(root)
    
    return True if res else False




if __name__ == "__main__":
    root = TreeNode(20)
    node1 = TreeNode(11)
    node2 = TreeNode(23)
    node3 = TreeNode(5)
    node4 = TreeNode(13)
    node5 = TreeNode(21)
    node6 = TreeNode(27)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6

    a = searchNode(root, 1)
    print(a)