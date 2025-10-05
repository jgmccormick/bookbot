def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def get_num_chars(file_contents):
    lower_case = file_contents.lower()
    character_count = {}
    for character in lower_case:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

