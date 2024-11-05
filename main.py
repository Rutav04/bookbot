def wordcount(contents):
    words = contents.split()
    return len(words)
def frankenstein_count(contents):
    return contents.lower().count("frankenstein")
def charcount(contents):
    alphabet = {}          
    for char in contents.lower():
        if char.isalpha():
            if char in alphabet:
                 alphabet[char] += 1
            else:
                alphabet[char] = 1
    return alphabet
def spcharcount(contents):
    alphabet = {}          
    for char in contents.lower():
        if not char.isalpha():
            if char in alphabet:
                 alphabet[char] += 1
            else:
                alphabet[char] = 1
    return alphabet
def print_character_counts(sorted_characters):
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        #print(contents)
        word_count = wordcount(contents)
        print (f"{word_count} words found in the document")
        frank_count = frankenstein_count(contents)
        #print(frank_count)
        characters = charcount(contents)
        #print (characters)
        specialchar = spcharcount(contents)
        #print (specialchar)
        character_list = [(char, count) for char, count in characters.items()]
        sorted_characters = sorted(character_list, key=lambda x: x[1], reverse=True)
        print_character_counts(sorted_characters)

        
        

main()