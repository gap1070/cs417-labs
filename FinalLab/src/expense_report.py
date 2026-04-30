"""Expense Report — starter code.

This script works. It reads transactions.csv, categorizes the rows,
and prints a report showing per-category totals.

It also has all of its logic crammed into one big main() function with
hard-coded filenames, a hard-coded category dict, and print() statements
woven into the calculations.

Your job is to refactor this code IN PLACE, by moving the right logic
into the four helper shapes below, in response to the change requests in
the README. Keep everything in this one file.

When you're done, the script should produce the SAME output (TOTAL = $613.87)
on the original inputs — the change requests should not change observable
behavior on the starting CSV.

DO NOT add any external libraries. Standard library only.
"""

import json
from pathlib import Path


# -----------------------------------------------------------------------------
# TODO Part 1 — fill these in. (See README "Part 1 — Add JSON support".)
# -----------------------------------------------------------------------------

def parse_csv(text: str) -> list[dict]:
    # converts csv text into row strcutures dictionaries 
    rows = []

    lines = text.strip().split("\n")

    # Skips the header 
    for line in lines[1:]:
        parts = line.split(",")

        # Skips the malformed rows 
        if len(parts) != 4:
            continue 

        date, vendor, amount, note = parts 

        rows.append({
            "date": date, 
            "vendor": vendor, 
            "amount": float(amount), 
            "note": note, 
        })

    return rows 

def parse_json(text: str) -> list[dict]:
    # converts the JSON strings into CSV 
    data = json.loads(text)

    rows = []

    for item in data:
        rows.append({
            "date": item["date"], 
            "vendor": item["vendor"], 
            "amount": float(item["amount"]), 
            "note": item["note"], 
        })

    return rows 

# -----------------------------------------------------------------------------
# TODO Part 2 — fill this in. (See README "Part 2 — Configurable categories".)
# -----------------------------------------------------------------------------

def categorize(vendor: str, categories: dict) -> str:
    # makes the vendors so they arent case sensitive 
    vendor_upper = vendor.upper()

    # checks all the categories and their keywords 
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in vendor_upper:
                return category 
    
    # returns the default category if nothing else matches 
    return "other"


# -----------------------------------------------------------------------------
# TODO Part 3 — fill this in. (See README "Part 3 — A pure pipeline".)
# -----------------------------------------------------------------------------

def build_report(rows: list[dict], categories: dict) -> dict:
    # computes the total for every category 
    totals = {}

    for row in rows:
        vendor = row["vendor"]
        amount = float(row["amount"])

        category = categorize(vendor, categories)

        # Gets the totals fof the categories safely
        totals[category] = totals.get(category, 0.0) + amount 

    return totals 


# -----------------------------------------------------------------------------
# main() — I/O lives here. Once Parts 1-3 are done, this should shrink to
# just the I/O glue: read files, call parse_*, call build_report, print.
# Right now it has everything inline.
# -----------------------------------------------------------------------------

def main():
    # reads the files 
    with open("data/transactions.csv") as f:
        text = f.read()
    
    # Parses the CSv into a more structured data set 
    rows = parse_csv(text)

    # Loads the different categories from the configuration file 
    categories = json.loads(Path("data/categories.json").read_text())

    # Builds the totals using logic 
    totals = build_report(rows, categories)

    # prints the results 
    print("=== Expense Report ===")

    for cat, total in sorted(totals.items()):
        print(f"  {cat:<15} ${total:>8.2f}")
        
    print(f"  {'TOTAL':<15} ${sum(totals.values()):>8.2f}")


if __name__ == "__main__":
    main()