def read_book(book_text):
    words = book_text.split()
    return (words)

def count_letters(book_text):
    lowered_text = book_text.lower()
    text_dict = {}
    for letter in lowered_text:
        if letter not in text_dict:
            text_dict[letter] = 1
        else:
            text_dict[letter] = text_dict[letter] + 1

    return text_dict

def sort_on(d):
    return d["num"]

def print_report(text_dict):
    sorted_dict = []
    #sorted_dict.sort(reverse=True, key=sorted_dict)

    for letter in text_dict:
        if letter.isalpha():
            sorted_dict.append({"char": letter, "num": text_dict[letter]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count = len(read_book(file_contents))

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words were found in the document\n")

        sorted_list = print_report(count_letters(file_contents))
        for letter in sorted_list:
            print(f"The '{letter['char']}' character appears {letter['num']} times")

        print("--- End report ---")

main()