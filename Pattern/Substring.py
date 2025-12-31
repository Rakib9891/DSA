# arr = "My name is Rakib name"
# res = arr.find('me')
# print(res)

def dfs_traverse_top_to_bottom():
    rows, cols = 3, 3
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            (r, c) in visited
        ):
            return

        visited.add((r, c))
        print((r, c), end=" ")

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # start DFS from top row
    for c in range(cols):
        dfs(0, c)


dfs_traverse_top_to_bottom()