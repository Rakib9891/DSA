class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def listToBinaryTRee(arr, left, right):
    arr.sort()

    def dfs(arr, left, right):
        if left > right: return None

        mid = (left + right) // 2
        root = TreeNode(arr[mid])
        root.left = dfs(arr, left, mid - 1)
        root.right = dfs(arr, mid + 1, right)
        return root
    return dfs(arr, left, right)

# For printing Tree 
def dfs(root):
    if not root: return
    print(root.val, end="->")
    dfs(root.left)
    dfs(root.right)

if __name__ == "__main__":
    arr = [5, 6, 1, 7, 8, 2, 3, 4]
    left = 0
    right = len(arr)-1
    root = listToBinaryTRee(arr, left, right)
    b = dfs(root)