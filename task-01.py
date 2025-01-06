from typing import List, Tuple


def find_min_max(numbers: List[float]) -> Tuple[float, float]:
    def recursive_min_max(start: int, end: int) -> Tuple[float, float]:
        if start == end:
            return numbers[start], numbers[start]

        if end == start + 1:
            return (
                min(numbers[start], numbers[end]),
                max(numbers[start], numbers[end]),
            )

        mid = (start + end) // 2
        left_min, left_max = recursive_min_max(start, mid)
        right_min, right_max = recursive_min_max(mid + 1, end)

        return (min(left_min, right_min), max(left_max, right_max))

    if not numbers:
        raise ValueError("Масив не може бути порожнім")

    return recursive_min_max(0, len(numbers) - 1)


if __name__ == "__main__":
    numbers = [3, 5, 2, -5, 1, 8, 0, 9]
    print(find_min_max(numbers))
