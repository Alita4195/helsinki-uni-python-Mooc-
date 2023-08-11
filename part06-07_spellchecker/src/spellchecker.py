# write your solution here
with open ("wordlist.txt") as new_file:
    word_list=[]
    for line in new_file:
        line = line.replace("\n", "")
        word_list.append(line)

text=input("Write text:")
tagged_text = ""
words = text.split()  #print out are list of strings

for word in words:
    if word.lower() not in word_list:  # Convert word to lowercase for case-insensitive comparison
        tagged_word = "*" + word + "*"  # Tag the misspelled word with asterisks
        tagged_text += tagged_word + " "
    else:
        tagged_text += word + " "
print(tagged_text)



    
