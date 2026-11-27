"""Summarize category values in a UTF-8 CSV file."""

import csv
from os import PathLike


def summarize(path: str | PathLike[str]) -> dict[str, int]:
    """Return counts of nonblank, trimmed values in the CSV's category column.

    Raises:
        ValueError: If the CSV header does not contain a ``category`` column.
    """
    with open(path, encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None or "category" not in reader.fieldnames:
            raise ValueError("CSV is missing the required 'category' column")

        counts: dict[str, int] = {}
        for row in reader:
            value = (row.get("category") or "").strip()
            if value:
                counts[value] = counts.get(value, 0) + 1

        return counts
