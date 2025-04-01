from stats import word_count

# Takes file path as input and returns file contents as a string
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
# main
def main():
    saved_book = get_book_text("books/frankenstein.txt")
    num_words = word_count(saved_book)
    print(f"{num_words} words found in the document")


main()
