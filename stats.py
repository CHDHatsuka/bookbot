def count_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def count_characters(text):
    num_characters = {}
    for character in text.lower():
        if character in num_characters:
            #if in, then increase the count of the matching key by 1
            num_characters[character] = num_characters[character] +1
        else:
            #if not in, then create a key with current iteration and
            # start a counter at 1
            num_characters[character] = 1
    return num_characters

#if you want to sort by a different key, change return
def choose_sort_key(list_item):
    return list_item["num"]

#convert the return dictionary from count_characters into a list
# where each item is a dictionary with a clearly labeled key/value pair
def dictionary_to_list(dictionary):
    list_of_dicts = []

    for ch, num in dictionary.items():
        list_of_dicts.append({"char": ch, "num": num})

    list_of_dicts.sort(key=choose_sort_key, reverse=True)

    return list_of_dicts
