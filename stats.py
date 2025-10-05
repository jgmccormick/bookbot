def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_sorted(chars):
    chars_sorted = []
    for char, num in chars.items():
        char_dict = {"char": char, "num": num}
        chars_sorted.append(char_dict)

    def sort_on(items):
        return items["num"]

    chars_sorted.sort(reverse=True, key=sort_on)
    return chars_sorted

