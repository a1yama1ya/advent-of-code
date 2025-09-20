import os


class Grid:
    def __init__(self, filename: str):
        with open(filename) as file:
            self.grid = [list(line.strip()) for line in file]

    def find_marker(self) -> tuple[int, int]:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "^":
                    return (i, j)
        raise RuntimeError("Marker not found")

    @property
    def rows(self) -> int:
        return len(self.grid)

    @property
    def cols(self) -> int:
        return len(self.grid[0])

    def __getitem__(self, position: tuple[int, int]) -> str:
        return self.grid[position[0]][position[1]]

    def __setitem__(self, position: tuple[int, int], value: str) -> None:
        self.grid[position[0]][position[1]] = value

    def count(self) -> int:
        total = 0
        for row in self.grid:
            total += sum(1 for cell in row if cell == "X")
        return total


class Guard:
    DIRECTION = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    TURN = {"^": ">", ">": "v", "v": "<", "<": "^"}

    def __init__(self, position: tuple[int, int]):
        self.position = position

    def move(self, grid: Grid) -> bool:
        direction = self.DIRECTION[grid[self.position]]

        new_pos = (self.position[0] + direction[0], self.position[1] + direction[1])
        if new_pos[0] < 0 or new_pos[0] >= grid.rows or new_pos[1] < 0 or new_pos[1] >= grid.cols:
            grid[self.position] = "X"
            return False

        if grid[new_pos] == "#":
            grid[self.position] = self.TURN[grid[self.position]]
            return True

        grid[new_pos] = grid[self.position]
        grid[self.position] = "X"
        self.position = new_pos
        return True


def main():
    grid = Grid(os.path.join(os.path.dirname(os.path.abspath(__file__)), "day6_1_data.csv"))
    guard = Guard(grid.find_marker())

    while guard.move(grid):
        pass

    print(f"total: {grid.count()}")

if __name__ == "__main__":
    main()
