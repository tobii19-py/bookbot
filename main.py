def main():
    path = "books/frankenstein.txt"
    book = get_book(path)
    word_count = get_book_words(book)
    char_dict = get_chars_count(book)
    sorted_list = get_report(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for char_info in sorted_list:
        print(f"The '{char_info["char"]}' character was found {char_info["count"]} times")

    print("--- End report ---")

def get_book(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(book):
    words = book.split()
    return len(words)

def get_report(char_dict):
    char_list = []

    for key, val in char_dict.items():
        if key.isalpha():
            char_list.append({"char": key, "count": val})
    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list

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