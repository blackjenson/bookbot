import sys
from stats import count_words
from stats import count_chars
from stats import sorted_dict
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    book_contents = get_book_text(bookpath)
    book_word_count = count_words(book_contents)
    book_char_count = count_chars(book_contents)
    report_one = sorted_dict(book_char_count)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {bookpath}...')
    print('----------- Word Count ----------')
    print(f'Found {book_word_count} total words')
    print('--------- Character Count -------')
    for item in report_one:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
        return book_contents

main()
