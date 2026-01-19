def count_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def count_characters(text):
    num_chars_dict = {}
    for character in text.lower():
        if character in num_chars_dict:
            #if in, then increase the count of the matching key by 1
            num_chars_dict[character] = num_chars_dict[character] +1
            #consider explaining the nature of the data on the name (eg _dict, _list...)
        else:
            #if not in, then create a key with current iteration and
            # start a counter at 1
            num_chars_dict[character] = 1
    return num_chars_dict

#if you want to sort by a different key, change return
def choose_sort_key(list_item):
    return list_item["num"]

#convert the return dictionary from count_characters into a list
# where each item is a dictionary with a clearly labeled key/value pair
def dictionary_to_list(num_chars_dict):
    list_of_char_dicts = []

    for ch, num in num_chars_dict.items():
        list_of_char_dicts.append({"char": ch, "num": num})

    list_of_char_dicts.sort(key=choose_sort_key, reverse=True)

    return list_of_char_dicts
