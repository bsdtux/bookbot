import sys
from stats import get_num_words, get_character_count, sort_character_count

def get_book_text(fp: str) -> str:
    with open(fp, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    character_count = sort_character_count(get_character_count(book_text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch in character_count:
        print(f"{ch['char']}: {ch['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()