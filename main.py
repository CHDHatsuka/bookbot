import sys
#keeping stat tracker functions in another file to keep code clean
from stats import count_words,count_characters,dictionary_to_list

#get the book text
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    #check if the correct usage of this program happened. Need to run it like described.
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

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

    for ch_dict in list_of_chs:
        if ch_dict["char"].isalpha() == True:
            print(f"{ch_dict["char"]}: " + f"{ch_dict["num"]}")
        else:
            continue

if __name__ == "__main__":
    main()
