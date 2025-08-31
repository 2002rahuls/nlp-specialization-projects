from utils import edit_distance

def load_dictionary(path='dictionary.txt') -> list:
  with open(path,'r') as file:
    return [line.strip() for line in file.readlines()]
  
def get_corrections(word: str, dictionary: list, max_suggestions=3) -> list:
    distances = [(dict_word, edit_distance(word, dict_word)) for dict_word in dictionary]
    distances.sort(key=lambda x: x[1])
    return [word for word, dist in distances[:max_suggestions]]
