# Write your solution here
def no_vowels(my_string):
    
    for item in my_string:
        if item=="a" or item=="o" or item=="e" or item=="i" or item=="u": 
            my_string=my_string.replace(item,"")
            
    print (my_string)
if __name__ == "__main__":
    no_vowels("abc")
    no_vowels("testword")