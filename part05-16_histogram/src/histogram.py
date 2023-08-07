# Write your solution here
def histogram(word:str):
    groups={}
    index=0
    while index<len(word):
        letter=word[index]
        if letter not in groups:
            groups[letter]=(letter+" *")
        else:
            groups[letter]=groups[letter]+("*")
        index+=1
    for key, value in groups.items():
        print(value)
if __name__=="__main__":
    word="abba"
    groups=histogram(word)



            

