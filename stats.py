def get_num_words(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> dict[str, int]:
    characters = {}
    for ch in text:
        ch = ch.lower()
        if ch not in characters:
            characters[ch] = 0
        characters[ch] += 1
    return characters

def sort_character_count(unsorted: dict[str, int]) -> list[dict[str, int]]:
    sorted_items = [{"char": key, "num": value} for key, value in unsorted.items() if key.isalpha()]
    return sorted(sorted_items, key=lambda x: x["num"], reverse=True)
