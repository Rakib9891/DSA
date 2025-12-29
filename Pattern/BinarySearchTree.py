from collections import deque
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def dfs(node):
    if not node: return
    
    print(node.val, end="->")
    
    dfs(node.left)
    dfs(node.right)

def bfs(root):
    if not root: return

    q = deque([root])
    while q:
        node =  q.popleft()
        print(node.val, end="->")
  
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
   
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

# bfs(root)
# dfs(root)

