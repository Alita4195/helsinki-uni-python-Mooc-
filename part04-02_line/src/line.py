# Write your solution here
# You can test your function by calling it within the following block
def line(a,b):
    if b=="":
        print(a*"*")
    else:
        print(a*b[0])
if __name__ == "__main__":
    line(10, "LOL")
    line(5, "XXX")
    line(3, "*")
    line(5, "")
