from stats import get_num_words, get_chars_dict, chars_dict_sorted

def main():
    book_path = "books/frankenstein.txt"
    # book_path = "README.md"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = chars_dict_sorted(chars_dict)
    print(("="*12) + " BOOKBOT " + ("="*12))
    print("Analyzing book found at books/frankenstein.txt")
    print(("-"*11) + " Word Count " + ("-"*11))
    print(f"Found {num_words} total words")
    print(("-"*9) + " Character Count " + ("-"*9))
    for d in sorted_chars:
        if d["char"].isalpha() is True:
            print(f'{d["char"]}: {d["num"]}')
    print(("="*13) + " END " + ("="*13))

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
