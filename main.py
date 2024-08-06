def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_words(text)
    chars_dict = charDict(text)
    sorted_list = sortedList(chars_dict)
    
    print(f"Report of {book_path}")
    print(f"{words} words found in the document.")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

def sort_on(unsorted):
    return unsorted["num"]

def sortedList(cdict):
    sorted_list = []
    for ch in cdict:
        sorted_list.append({"char": ch, "num": cdict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def charDict(words):
    chars = {}
    for x in words:
        lowered = x.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def lowered_string(text):
    lowerWords = text.lower()
    return lowerWords

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

