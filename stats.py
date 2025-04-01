# Takes text from book as string and returns number of words in the string.
def word_count(text):
    get_book_text()
    split_text = text.split()
    return len(split_text)