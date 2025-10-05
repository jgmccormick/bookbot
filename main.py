from stats import get_num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    num_words = get_num_words(file_contents)
    return print(f"Found {num_words} total words")

main("books/frankenstein.txt")