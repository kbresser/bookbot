import sys

from stats import (
    num_words,
    char_count,
    sort_char
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = num_words(text)
    char = char_count(text)
    sort = sort_char(char)
    print_report(book_path, word_count, sort)

def print_report(book_path, word_count, sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for l in sort:
        if l["char"].isalpha():
            print(f"{l['char']}: {l['count']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()