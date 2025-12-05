from pathlib import Path


def get_fresh_data() -> list[list[int]]:
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "fresh_ids.txt"
    data = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            start, end = line.split("-")
            data.append([int(start), int(end)])
    return data


def get_availability_data() -> list[int]:
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "available_ids.txt"
    data = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(int(line))
    return data


class TheTotal:
    def __init__(self):
        self.count = 0

    def increase(self, amount: int = 1):
        self.count += amount

    def get_count(self) -> int:
        return self.count


def is_it_fresh(fresh_ids: list[list[int]], available_id: int) -> bool:
    for range in fresh_ids:
        if available_id >= range[0] and available_id <= range[1]:
            return True
    return False


def find_fresh_ingridients():
    fresh_available_num = TheTotal()
    fresh_ids = get_fresh_data()
    available_ids = get_availability_data()
    for id in available_ids:
        if is_it_fresh(fresh_ids, id):
            fresh_available_num.increase()
    return fresh_available_num.get_count()


if __name__ == "__main__":
    print(find_fresh_ingridients())
