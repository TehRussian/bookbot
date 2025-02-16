def main():
    book_path = "books/frankenstein.txt"
    book_string = get_book_text(book_path)
    num_words = get_word_count(book_string)
    num_letters = get_letter_count(book_string)
    alphabet_list_lower = list(map(chr, range(97, 123)))
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    for letter_index in range(len(alphabet_list_lower)):
        print(f"The '{alphabet_list_lower[letter_index]}' character was found {num_letters[alphabet_list_lower[letter_index]]} times")
    print("--- End report ---")
    
#Open file and return a string    
def get_book_text(path):
    with open(path) as f:
        return f.read()

#Get word cound from the string    
def get_word_count(book_string):
    book_split = book_string.split()
    return len(book_split)
        
#Get a dictionary with each letter/symbol count from the book
def get_letter_count(book_string):
    letter_dict = {}
    for letter in book_string.lower():
        if letter not in letter_dict:
            letter_dict.update({letter: 1})
        else:
            letter_dict[letter] += 1
    return letter_dict
    

main()