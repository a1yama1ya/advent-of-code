import os

def read_data() -> list[int | str]:
    data = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "day9_1_data.csv")) as file:
        for line in file:
            for index, char in enumerate(line.strip()):
                if int(index) % 2 == 0:
                    data.extend(int(index/2) for _ in range(int(char)))
                else:
                    data.extend("." for _ in range(int(char)))
    return data


def move_elements(data: list[int | str]) -> list[int | str]:
    current = 0
    last = len(data) - 1
    while current < last:
        if data[current] == ".":
            while data[last] == ".":
                last -= 1
            data[current] = data[last]
            last -= 1
        else:
            current += 1
    return data[:current + 1]


def find_total(moved: list[int | str]) -> int:
    return sum(index * element for index, element in enumerate(moved) if isinstance(element, int))


def main() -> None:
    data = read_data()
    moved = move_elements(data)
    print(find_total(moved))


if __name__ == "__main__":
    main()
