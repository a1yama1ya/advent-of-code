import os
from itertools import combinations


def load_order() -> list[list[str]]:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "day5order.csv")) as file:
        return [line.strip().split("|") for line in file]


def process_pages(order: list[list[str]]) -> list[list[str]]:
    correct = []
    order_set = {tuple(pair) for pair in order}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "day5pages.csv")) as file:
        for line in file:
            pages = line.strip().split(",")
            if not any((pair[1], pair[0]) in order_set for pair in combinations(pages, 2)):
                correct.append(pages)
    return correct


def calculate_total(correct: list[list[str]]) -> int:
    return sum(int(item[len(item) // 2]) for item in correct)


def main():
    order = load_order()
    correct = process_pages(order)
    total = calculate_total(correct)
    print(f"total: {total}")


if __name__ == "__main__":
    main()
