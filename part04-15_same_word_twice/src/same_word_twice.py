# Write your solution here
sentence =[]
n=0
while True:
    userInput = input("Word:")
    n+=1
    if userInput in sentence:
        break
    sentence.append(userInput)

print(f"You typed in {n-1} different words")


    

    


        
        