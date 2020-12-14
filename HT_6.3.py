
def NumberOfCharacters(string, character):
    k = 0
    string = string.split(" ")
    for i in range(len(string)):
        while character in string[i]:
            k += 1
            string[i] = string[i][:string[i].find(character)] + string[i][string[i].find(character) + len(character):]
    return k



string = input("Enter a string: ")
character = input("Enter the character you'd like to count in your string: ")
print(NumberOfCharacters(string, character))