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


def find_max_joltage(bank: str) -> int:
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            pair = bank[i] + bank[j]
            if int(pair) > max_joltage:
                max_joltage = int(pair)
    return max_joltage


def find_total_joltage() -> int:
    result = TheTotal()
    banks = get_data()

    for bank in banks:
        result.increase(find_max_joltage(bank))
    return result.get_count()


if __name__ == "__main__":
    print(find_total_joltage())
