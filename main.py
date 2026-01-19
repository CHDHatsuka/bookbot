import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

#keeping stat tracker functions in another file to keep code clean
from stats import count_words

from stats import count_characters

from stats import dictionary_to_list

def main():
    text = get_book_text(sys.argv[1])
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}")

    #count the words and show me the count
    print(f"----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    #count the characters and show me the count
    print("--------- Character Count -------")
    num_characters = count_characters(text)
    ##print(num_characters)

    #sort alphabetical characters from highest to lowest and show me
    # the clean list
    list_of_chs = dictionary_to_list(num_characters)

    for ch in list_of_chs:
        if ch["char"].isalpha() == True:
            print(f"{ch["char"]}: " + f"{ch["num"]}")
        else:
            continue

main()
