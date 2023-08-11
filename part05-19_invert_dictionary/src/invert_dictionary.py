# Write your solution here
def invert(dictionary: dict):  #2nd attempt, success!
    inv_dic = {}
    for k, v in dictionary.items():
        inv_dic[v]=k
    dictionary.clear()
    for k, v in inv_dic.items():
        dictionary[k]=v
    print(dictionary)

if __name__=="__main__":
    dictionary={1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(dictionary)
