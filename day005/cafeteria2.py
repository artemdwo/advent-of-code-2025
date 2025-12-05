from pathlib import Path


def get_fresh_data() -> list[tuple[int, int]]:
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "fresh_ids.txt"
    data = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            start, end = line.split("-")
            data.append((int(start), int(end)))
    return data


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []

    ranges.sort(key=lambda r: r[0])

    merged: list[tuple[int, int]] = []
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))
    return merged


def find_all_fresh_ingridients():
    fresh_ids = get_fresh_data()

    merged = merge_ranges(fresh_ids)

    total_fresh_ids = sum(end - start + 1 for start, end in merged)

    return total_fresh_ids


if __name__ == "__main__":
    print(find_all_fresh_ingridients())
