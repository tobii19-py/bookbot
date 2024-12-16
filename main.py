def main():
    path = "books/frankenstein.txt"
    book = get_book(path)
    count = get_book_words(book)
    print(count)

def get_book(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(book):
    words = book.split()
    return len(words)

main()