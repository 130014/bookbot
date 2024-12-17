def get_cha():
    # Read the contents of a file and return as words
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        words = file_contents.split()
    return words

def count(words):
    # Count and return as dictionary
    char_count = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    return char_count
    
def main():
    words = get_cha()
    char_count = count(words)
    for k, v in char_count.items():
        print(f"The '{k}' character was found {v} times")

if __name__ == "__main__":
    main()