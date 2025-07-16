import sys
from pathlib import Path

from stats import get_num_chars, get_num_words, get_sorted_dict_list, print_report


def main():
    if len(sys.argv) != 2:  # noqa: PLR2004
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1] or "books/frankenstein.txt"
    text = Path(filepath).read_text()
    num_words = get_num_words(text)
    char_counts_dict = get_num_chars(text)
    char_counts_list = get_sorted_dict_list(char_counts_dict)
    print_report(filepath, num_words, char_counts_list)


if __name__ == "__main__":
    main()
