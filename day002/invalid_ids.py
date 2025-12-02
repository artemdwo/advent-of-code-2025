from pathlib import Path
from typing import Generator


def get_data():
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "input.txt"

    with open(file_path, "r") as f:
        data = f.read().split(",")
    return data


class TheTotal:
    def __init__(self):
        self.count = 0

    def increase(self, amount: int):
        self.count += amount

    def get_count(self) -> int:
        return self.count


def parse_data(ranges: list[str]) -> Generator[tuple[int, int], None, None]:
    for part in ranges:
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split("-")
        yield int(start_str), int(end_str)


def is_invalid(id: int) -> bool:
    s = str(id)
    length = len(s)

    for sub_len in range(1, length // 2 + 1):
        if length % sub_len != 0:
            continue  # pattern must divide total length exactly

        repetitions = length // sub_len
        if repetitions < 2:
            continue  # must repeat at least twice

        pattern = s[:sub_len]
        if pattern * repetitions == s:
            return True

    return False


def find_invalid_ids() -> int:
    result = TheTotal()
    product_ids_raw = get_data()

    for range_start, range_end in parse_data(product_ids_raw):
        for id in range(range_start, range_end + 1):
            if is_invalid(id):
                result.increase(id)
    return result.get_count()


if __name__ == "__main__":
    print(find_invalid_ids())
