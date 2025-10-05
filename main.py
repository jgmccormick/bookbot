from stats import get_num_words, get_chars_dict

def main():
    book_path = "books/frankenstein.txt"
    # book_path = "README.md"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_chars_dict(text)
    print(f"Found {num_words} total words")
    print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
