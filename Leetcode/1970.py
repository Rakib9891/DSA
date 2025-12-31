# 1970. Last Day Where You Can Still Cross


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def bfs(m):
            grid = [[0 for _ in range(col)] for _ in range(row)]
            for i in range(m + 1):
                grid[cells[i][0] - 1][cells[i][1] - 1] = 1
            q = deque()

            for j in range(len(grid[0])):
                if grid[0][j] == 0:
                    q.append((0, j))

            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
             
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nc < col and
                        0 <= nr < row and
                        grid[nr][nc] != 1
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = 1
            return False
        
        res = 0
        l, r = 0, len(cells) - 1
        while l <= r:
            m = (l + r) // 2
           
            if bfs(m):
                res = m + 1
                l = m + 1
            else:
                r = m - 1

        return res