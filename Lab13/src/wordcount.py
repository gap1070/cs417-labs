"""Word counter using argparse."""
import argparse
from collections import Counter


def build_parser():
    parser = argparse.ArgumentParser(description="Word counting tool")
    
    parser.add_argument(
        "filename",
        help="text file to analyze"
    )

    parser.add_argument(
        "--ignore-case", "-i",
        action="store_true",
        help="lowercase all words before counting"
    )
    
    parser.add_argument(
        "--top", "-t", 
        type=int, 
        default=None,
        help="show top N most frequent words"
    )

    return parser
    
    # TODO: Add --min-length / -m (type=int, default=1)
    # TODO: Add --sort-by / -s (choices=["freq", "alpha"], default="freq")
    # TODO: Add --reverse / -r (action="store_true")


def analyze(filepath, ignore_case=False, top=None, min_length=1,
            sort_by="freq", reverse=False):
    with open(filepath, "r") as f:
        words = f.read().split()

    if ignore_case:
        words = [w.lower() for w in words]

    count = len(words)

    if top is None:
        return f"{filepath}: {count} words"
    
    counter = Counter(words)
    common = counter.most_common(top)

    result = f"{filepath}: {count} words\n\nTop {top} words:\n"

    for word, c in common:
        result += f"  {word}: {c}\n"

    return result.strip()
    
    # TODO: Filter out words shorter than min_length
    # TODO: Count total words
    # TODO: If top is None, return "<filename>: <count> words"
    # TODO: If top is set, find the most frequent words:
    #   - Use Counter(words).most_common() for frequency data
    #   - If sort_by == "alpha", sort alphabetically instead
    #   - If reverse, flip the order
    #   - Take the first 'top' entries
    #   - Return multi-line string:
    #       "<filename>: <count> words\n\nTop <N> words:\n  <word>: <count>\n  ..."
    pass


def main():
    parser = build_parser()
    args = parser.parse_args()

    result = analyze(
        args.filename,
        ignore_case=args.ignore_case,
        top=args.top
    )

    print(result)

if __name__ == "__main__":
    main()