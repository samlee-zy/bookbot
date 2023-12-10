def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    answer = get_char(text)
    storeAnswer = list(answer.items())
    storeAnswer.sort()
    for i in (storeAnswer):
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")
    # print(text)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char(texts):
    charFrequency = {}
    texts = texts.lower()
    for char in texts:
        if char in charFrequency:
            charFrequency[char] += 1
        elif char.isalpha():
            charFrequency[char] = 1
        else:
            continue
    return charFrequency

main()