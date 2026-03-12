"""Word counter using manual sys.argv parsing."""
import sys


def parse_args_manual(argv):
    if len(argv) < 2:
        print("Usage: wordcount_manual.py <filename>", file=sys.stderr)
        sys.exit[1]

    return argv[1]


def count_words(filepath):
    try:
        with open(filepath, "r") as f:
            words = f.read().split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: file '{filepath}' not found", file=sys.stderr)
        sys.exit(1)


def main():
    filename = parse_args_manual(sys.argv)
    count = count_words(filename)
    print(f"{filename}: {count} words")



if __name__ == "__main__":
    main()