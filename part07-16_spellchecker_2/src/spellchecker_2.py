# import difflib


# def get_close_matches(word, word_list):
#     return difflib.get_close_matches(word, word_list)

# with open ("wordlist.txt") as new_file:
#     word_list=[]
#     for line in new_file:
#         line = line.replace("\n", "")
#         word_list.append(line)
#         #print(word_list) 所有word组成的list

# text=input("Write text:")
# tagged_text = ""
# words = text.split()
# # print(words)  #print out are list of strings e.g.["I", "love", "python"]

# for word in words:
#     if word.lower() not in word_list:  # Convert word to lowercase for case-insensitive comparison
#         tagged_word = "*" + word + "*"  # Tag the misspelled word with asterisks
#         tagged_text += tagged_word + " "
#     else:
#         tagged_text += word + " "
# print(tagged_text)
# print("suggestions:" )
# with open("wordlist.txt") as new_file:
#     word_list = [line.strip() for line in new_file]


# for word in words:
#     if word.lower() not in word_list:
#         suggestions = get_close_matches(word, word_list)
#         if suggestions:
#             tagged_word = "*" + word + "*"
#             tagged_text += tagged_word + " "
#             suggestions_str = ", ".join(suggestions)
#             print(f"{word}: {suggestions_str}")
#     else:
#         tagged_text += word + " "

import difflib


def wordlist():
    words = []
    with open("wordlist.txt") as file:
        for rivi in file:
            words.append(rivi.strip())
    return words


words = wordlist()
sentence = input("write text: ")
error = []
for word in sentence.split(" "):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        error.append(word)
        print("*" + word + "* ", end="")

print() #这个block的方法很值得学习

print("suggestions:")
for word in error:
    suggestion_list = difflib.get_close_matches(word, words)
    suggestions = ", ".join(suggestion_list)
    print(f"{word}: {suggestions}")
