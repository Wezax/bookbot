def get_word_count_from_string(text:str) -> int:
    return len(text.split())

def get_unique_char_map_from_string(text:str) -> dict[str,int]: 
    char_dict: dict[str,int] = {}
    for char in text:
        char_to_lower: str = char.lower()
        if char_to_lower in char_dict:
            char_dict[char_to_lower] += 1
        else:
            char_dict[char_to_lower] = 1
    return char_dict

def sort_dict_by_character_count(char_dict:dict[str,int]) -> list[dict[str,str|int]]:
    sorted_list: list[dict[str,str|int]]= [] 
    for k in char_dict:
        sorted_list.append({"char": k, "num": char_dict[k]})
    sorted_list.sort(key=lambda d: d["num"], reverse=True)
    return sorted_list



