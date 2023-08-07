# Write your solution here
def dict_of_numbers(): #loops and dictionaries
    numbers={1:'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0: 'zero'}
    for i in range(100):
        if 20 < i <= 99:
            div = (i // 10) * 10 #整数
            mod = i % 10 #得到的是一个数除以另一个数的余数
            if mod != 0:
                numbers[i]= (numbers[div] + "-" + numbers[mod])
    return numbers
if __name__=="__main__":
    numbers = dict_of_numbers()
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])



        
        

        

    


