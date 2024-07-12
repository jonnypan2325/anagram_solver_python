import itertools
import os
import json

exit_words = {'q', 'exit', 'quit', 'close'}
def startup():
    if not os.path.exists('dictionary.json'):
        print("Dictionary file 'dictionary.json' not found. Please create a dictionary first.")
        print("Exiting ....")
        exit(1)  
    else:
        with open('dictionary.json', 'r') as file:
            valid_words = set(json.load(file))
            letters = new_word()
            return(letters,valid_words)
        
def new_word(letters = None):
        if letters is None:
            letters = input("Enter letters without spaces: ")
        return letters.lower()
                
def length_query():
    query = input('Words of what length? or enter new word: ')
    if query in exit_words:
        print("Exiting ....")
        exit()
    else:
        try:
            return int(query)
        except:
            return new_word(query)
    
def permutate(letters, length):
    return set([''.join(p) for p in itertools.permutations(letters, length)])

def check_valid(word, valid_words):
    return word in valid_words

def filter_valid_permutations(permutations, valid_words):
    return [word for word in permutations if check_valid(word, valid_words)]

def main():
    letters, valid_words = startup()
    user_input = letters
    while(user_input not in exit_words):
        length = length_query()
        if(type(length) != int):
            letters = length
            length = length_query()
        all_permutations = permutate(letters, length)

        valid_permutations = filter_valid_permutations(all_permutations, valid_words)  
        
        print(f"Valid anagrams of length {length} for '{letters}': {valid_permutations}")

    
if __name__ == "__main__":
    main()


