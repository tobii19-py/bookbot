def main():
    path = "books/frankenstein.txt"
    book = get_book(path)
    count = get_book_words(book)
    char_count = get_chars_count(book)
    print(count)
    print(char_count)

def get_book(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(book):
    words = book.split()
    return len(words)

def get_chars_count(book):
    char_dict = {}

    for ch in book:
        ch_lower = ch.lower()
    
        if ch_lower in char_dict:
            char_dict[ch_lower] += 1
        else:
            char_dict[ch_lower] = 1
    
    return char_dict

main()