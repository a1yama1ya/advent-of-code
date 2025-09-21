import os


def create_grid() -> list[str]:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "day8_1_data.csv")) as file:
        return [line.strip() for line in file]


def find_types_of_antenna(grid: list[str]) -> set[str]:
    return {cell for row in grid for cell in row if cell != "."}


def locations_of_antinodes_of_a_certain_type(grid: list[str], antenna: str) -> list[tuple[int, int]]:
    locations = [
        (i, j)
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == antenna
    ]

    return [
        (2*x1 - x2, 2*y1 - y2)
        for x1, y1 in locations
        for x2, y2 in locations
        if (x1, y1) != (x2, y2)
    ]


def all_locations_of_antinodes(grid: list[str], antennas: set[str]) -> set[tuple[int, int]]:
    return {loc for antenna in antennas for loc in locations_of_antinodes_of_a_certain_type(grid, antenna)}


def main() -> None:
    grid = create_grid()
    antennas = find_types_of_antenna(grid)
    antinode_locations = all_locations_of_antinodes(grid, antennas)
    count = sum(0 <= x < len(grid) and 0 <= y < len(grid[0]) for x, y in antinode_locations)
    print(count)


if __name__ == "__main__":
    main()
