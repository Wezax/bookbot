import sys
from stats import get_word_count_from_string, get_unique_char_map_from_string, sort_dict_by_character_count
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents: str = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath: str = sys.argv[1]
    text: str = get_book_text(filepath)
    number_of_words: int  = get_word_count_from_string(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    char_dict = get_unique_char_map_from_string(text)
    sorted_char_list = sort_dict_by_character_count(char_dict)
    for char_set in sorted_char_list:
        if isinstance(char_set["char"], str) and char_set["char"].isalpha():
            print(f'{char_set["char"]}: {char_set["num"]}')
    print("============= END ===============")

if __name__ == "__main__":
    main()
