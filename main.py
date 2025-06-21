import sys
from stats import get_num_words, get_num_char, sort_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents
      
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    extracted_text = get_book_text(file_path)
    num_words = get_num_words(extracted_text)
    char_count = get_num_char(extracted_text)
    sorted_list_dict = sort_char_count(char_count)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list_dict:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()