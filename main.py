def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def word_count(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    num_words = word_count(file_contents)
    return print(f"Found {num_words} total words")

main("books/frankenstein.txt")