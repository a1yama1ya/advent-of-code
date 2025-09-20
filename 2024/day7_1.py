import os


def import_data() -> list[str]:
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day7_1_data.csv")
    with open(data_path) as file:
        return [line.strip() for line in file]


def seperate_result_from_elements(data: list[str]) -> tuple[list[int], list[list[int]]]:
    elements = []
    results = []
    for line in data:
        result, element = line.split(":")
        elements.append([int(elem) for elem in element.split()])
        results.append(int(result))
    return results, elements


def create_all_possible_results(elements: list[list[int]]) -> list[set[int]]:
    all_possible_results = []
    for row in elements:
        possible_results = set()
        possible_results.add(row[0])
        for element in row[1:]:
            new_results = set()
            for result in possible_results:
                new_results.add(result + element)
                new_results.add(result * element)
            possible_results = new_results
        all_possible_results.append(possible_results)
    return all_possible_results


def main():
    data = import_data()
    results, elements = seperate_result_from_elements(data)
    all_possible_results = create_all_possible_results(elements)
    sum_of_correct_results = 0
    for result, possible_results in zip(results, all_possible_results):
        if result in possible_results:
            sum_of_correct_results += result
    print(sum_of_correct_results)


if __name__ == "__main__":
    main()
