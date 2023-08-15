"""https://fivethirtyeight.com/features/can-you-break-the-riddler-bank/"""
import numpy as np

MAZE = [
    [6, 2, 1, 3, 6, 1, 7, 7, 4, 3],
    [2, 3, 4, 5, 7, 8, 1, 5, 2, 3],
    [1, 6, 1, 2, 5, 1, 6, 3, 6, 2],
    [5, 3, 5, 5, 1, 6, 7, 3, 7, 3],
    [1, 2, 6, 4, 1, 3, 3, 5, 5, 5],
    [2, 4, 6, 6, 6, 2, 1, 3, 8, 8],
    [2, 4, -1, 2, 3, 6, 5, 2, 4, 6],
    [3, 1, 7, 6, 2, 3, 1, 5, 7, 7],
    [6, 1, 3, 6, 4, 5, 4, 2, 2, 7],
    [6, 7, 5, 7, 6, 2, 4, 1, 9, 1],
]


class MazeSolver:
    def __init__(self, maze) -> None:
        maze = np.array(maze, dtype=int)
        assert all(len(maze[i]) == len(maze[0]) for i in range(1, len(maze)))
        assert all(
            isinstance(maze[i, j], (int, np.int64))
            for i in range(len(maze))
            for j in range(len(maze[0]))
        )
        assert (maze == -1).sum() == 1, "There must be exactly one exit"
        self.maze = maze
        self.start = (len(self.maze) - 1, 0)
        self.end = (np.where(self.maze == -1)[0][0], np.where(self.maze == -1)[1][0])
        self.nb_rows = len(self.maze)
        self.nb_cols = len(self.maze[0])

    def solve(self):
        queue = [(self.start, [self.start])]
        while queue:
            cell, path = queue.pop(0)
            if cell in path[:-1]:
                continue
            if cell == self.end:
                print(path)
                break
            val = self.maze[cell]
            row, col = cell

            left = row, col - val
            if left[1] >= 0:
                queue.append((left, path + [left]))

            right = row, col + val
            if right[1] < self.nb_cols:
                queue.append((right, path + [right]))

            down = row + val, col
            if down[0] < self.nb_rows:
                queue.append((down, path + [down]))

            up = row - val, col
            if up[0] >= 0:
                queue.append((up, path + [up]))

        else:
            print("Unsolvable")


if __name__ == "__main__":
    solver = MazeSolver(MAZE)
    solver.solve()
