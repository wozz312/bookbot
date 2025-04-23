from stats import num_words
from stats import letter_count
from stats import sort_list
import sys

def get_book_text (filepath):
    with open(filepath) as f:
        file = f.read()
    return file

def validate_arguments():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    validate_arguments()
    book_text = get_book_text (sys.argv[1])
    
    num_count = num_words(book_text)
    char_counts = letter_count(book_text)
    sorted_chars = sort_list(char_counts)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book_text)} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_info in sorted_chars:
        char = char_info["character"]
        count = char_info["count"]
        print(f"{char}: {count}")
    
    print("============= END ===============")


main()