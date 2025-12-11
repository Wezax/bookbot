def get_word_count_from_string(text): 
    return len(text.split())

def get_unique_char_map_from_string(text):
    char_dict = {}
    for char in text:
        char_to_lower = char.lower()
        if char_to_lower in char_dict:
            char_dict[char_to_lower] += 1
        else:
            char_dict[char_to_lower] = 1
    return char_dict

def sort_dict_by_character_count(char_dict):
    sorted_list= []
    for k in char_dict:
        sorted_list.append({"char": k, "num": char_dict[k]})
    sorted_list.sort(key=lambda d: d["num"], reverse=True)
    return sorted_list



