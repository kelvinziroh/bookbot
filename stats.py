def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    # Lower the case of the entire text
    text = text.lower()
    # Initialize the character count
    character_count = {}
    for char in text:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] +=1
    return character_count

def sort_char_count(ccount_dict):
    # Initialize an empty list
    dict_list = []
    # For each character in the dictionary
    for char in ccount_dict:
        if not char.isalpha(): # Exclude non-alphabetic characters
            continue
        dict_list.append({"char": char, "num": ccount_dict[char]})
    
    def sort_on(items):
        return items["num"]
    
    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list