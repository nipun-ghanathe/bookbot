from typing import Any


def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_chars(text: str) -> dict[str, int]:
    text = text.lower()
    chars = set(text)
    return {char: text.count(char) for char in chars}


def get_sorted_dict_list(char_counts: dict[str, int]) -> list[dict[str, Any]]:
    count_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    count_list.sort(reverse=True, key=lambda d: d["num"])  # type: ignore[arg-type,return-value]
    return count_list


def print_char_counts(char_counts_list: list[dict[str, Any]]) -> None:
    for char_dict in char_counts_list:
        if not char_dict["char"].isalpha():
            continue
        print(f"{char_dict['char']}: {char_dict['num']}")


def print_report(
    filepath: str, num_words: int, char_counts_list: list[dict[str, Any]]
) -> None:
    print(" BOOKBOT ".center(34, "="))
    print(f"Analyzing book found at {filepath}...")
    print(" Word Count ".center(34, "-"))
    print(f"Found {num_words} total words")
    print(" Character Count ".center(34, "-"))
    print_char_counts(char_counts_list)
    print(" END ".center(34, "="))
