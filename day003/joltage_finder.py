from pathlib import Path


def get_data():
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "input.txt"

    with open(file_path, "r") as f:
        data = f.read().splitlines()
    return data


class TheTotal:
    def __init__(self):
        self.count = 0

    def increase(self, amount: int):
        self.count += amount

    def get_count(self) -> int:
        return self.count


def find_max_joltage(bank: str, length: int = 12) -> int:
    n = len(bank)
    if length >= n:
        return int(bank)

    to_remove = n - length
    stack = []

    for d in bank:
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    if to_remove > 0:
        stack = stack[:-to_remove]

    result_str = "".join(stack[:length])
    return int(result_str)


def find_total_joltage() -> int:
    result = TheTotal()
    banks = get_data()

    for bank in banks:
        result.increase(find_max_joltage(bank))
    return result.get_count()


if __name__ == "__main__":
    print(find_total_joltage())
