def count_words(book_contents):
    words = book_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count
    
def count_chars(book_contents):
    chars_dict = {}
    words = book_contents.split()
    for word in words:
        words_to_chars = list(word.lower())
        for char in words_to_chars:
            if char in chars_dict:
                chars_dict[char] +=1
            else:
                chars_dict[char] = 1
    return chars_dict

def sort_on(items):
    return items["num"]

def sorted_dict(book_char_count):
    dict_list_combine = []
    for key, value in book_char_count.items():
        dict_list = {"char" : key, "num" : value}
        dict_list_combine.append(dict_list)
    dict_list_combine.sort(reverse=True, key=sort_on)
    return dict_list_combine

