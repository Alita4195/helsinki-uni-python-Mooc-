# Write your solution here
def anagrams(word_1, word_2):
    in_order_1=sorted(word_1)
    in_order_2=sorted(word_2)
    if in_order_1==in_order_2:
        return True
    else:
        return False
if __name__ == "__main__":
    print(anagrams("tame", "meta"))
    