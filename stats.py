def num_words(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    letters = {}
    for c in book_text:
        case = c.lower()
        if case in letters:
            letters[case] += 1
        else:
            letters[case] = 1
    return letters

def sort_char(input):
    chars_list = []
    for char, count in input.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    chars_list.sort(key=sort_on, reverse=True)
    return chars_list
