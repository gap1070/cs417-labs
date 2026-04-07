"""
Lab 18: Working with CSV and JSON Files

Read, write, and convert between CSV and JSON formats.
"""

import csv
import json
from pathlib import Path


def read_csv(filepath: str) -> list[dict]:
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_json(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def write_csv(filepath: str, data: list[dict], fieldnames: list[str]) -> None:
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def write_json(filepath: str, data) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def csv_to_json(
    csv_path: str,
    json_path: str,
    type_hints: dict[str, type] | None = None,
) -> None:
    """Convert a CSV file to a JSON file.

    CSV stores everything as strings. The type_hints parameter lets you
    specify which columns should be converted to other types before
    writing JSON.

    TODO (Task 5a):
    - Read the CSV file using your read_csv function
    - For each row, convert values according to type_hints
      (e.g., if type_hints={"grade": int}, convert row["grade"] to int)
    - Write the result using your write_json function

    Args:
        csv_path: Path to the input CSV file.
        json_path: Path for the output JSON file.
        type_hints: Optional dict mapping column names to types.
                    Example: {"grade": int, "gpa": float}

    Example:
        >>> csv_to_json("roster.csv", "roster.json", type_hints={"grade": int})
    """
    # TODO: Implement this function
    pass


def json_to_csv(
    json_path: str,
    csv_path: str,
    fieldnames: list[str],
) -> None:
    """Convert a JSON file to a CSV file.

    JSON can hold nested data that doesn't fit in flat CSV columns.
    Only the keys listed in fieldnames are included — nested or
    unlisted fields are silently skipped.

    TODO (Task 5b):
    - Read the JSON file using your read_json function
    - For each record, build a new dict with only the fieldnames keys
    - Write the result using your write_csv function

    Args:
        json_path: Path to the input JSON file.
        csv_path: Path for the output CSV file.
        fieldnames: Which top-level keys to include as columns.

    Example:
        >>> json_to_csv("roster.json", "roster.csv", ["name", "email", "grade"])
        # "tags" field from JSON is skipped — it can't be a flat CSV column
    """
    # TODO: Implement this function
    pass