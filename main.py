def main():
    # defines the book path
    book_path = "books/frankenstein.txt"
    # stores the book into text var
    text = get_book_text(book_path)
    # uses word_count func to count number of words
    num_words = word_count(text)
    # uses count_letters func to get dict of letter:count
    letter_dict = count_letters(text)
    # uses chars_dict_to_sorted_list func to convert dict to sorted list
    sorted_list = convert_dict_to_list(letter_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_list:
        # removes anything not AZaz
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(str):
    new_str = str.split()
    return len(new_str)

# Sorts list by 
def sort_on(d):
    return d["num"]

def count_letters(str):
    new_dict = {}
    new_str = str.replace(" ", "").lower()
    for letter in new_str:
        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1
    return new_dict

def convert_dict_to_list(dict):
    sorted_list = []
    for letter in dict:
        # "num" must be present here for sort_on func to work properly
        sorted_list.append({"char": letter, "num": dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()