
print("1 - Add word, 2 - Search, 3 - Quit")

while True:

    function = int(input("Function: "))
    if function == 1:
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        couple = finnish_word + "-" + english_word
        print("Dictionary entry added")
        with open("dictionary.txt", "a") as my_file:
            my_file.write(couple + "\n")  # Add a newline character after each entry
    if function == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                line = line.strip()
                if search in line:
                    print(line)
    if function == 3:
        print("Bye!")
        break