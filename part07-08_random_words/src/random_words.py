# Write your solution here
# def words(n: int, beginning: str):
#     word_list=[]
#     with open("words.txt")as my_file:
#         for line in my_file:
#             line=line.strip()

#             while n>0:
#                 if beginning in line:
#                    word_list.append(line)
#                 n-=1
#         print(word_list)

# word_list = words(3, "ca")
import random

def words(n: int, beginning: str):
    word_list = []
    random_word_list=[]
    count = 0  # Variable to keep track of the number of words found

    with open("words.txt") as my_file:
        for line in my_file:
            line=line.strip()
            if line.startswith(beginning):
                word_list.append(line) #输出所有"ca"开头的单词

        if len(word_list)<n:
            raise ValueError("Not enough words beginning with the specified string.")
        
        while count< n:
            word = random.choice(word_list)
            
            if word in random_word_list:
                continue
            random_word_list.append(word)
            count+=1
        return (random_word_list)



        #     if len(available_words) < n:
        #         raise ValueError("Not enough words beginning with the specified string.")

        #     while count < n:
        #         word = random.choice(available_words)
        #         available_words.remove(word)
        #         word_list.append(word)
        #         count += 1

        # return word_list
if __name__ == "__main__":
    result = words(3, "ca")
    print(result)




