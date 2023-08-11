# Write your solution here
# You can test your function by calling it within the following block
def same_chars(a,b,c):
    f=len(a)
    if b<f and c<f and a[b]==a[c]:
        return True

    elif b>=f or c>=f:
        return False
    else:
        return False
if __name__ == "__main__":
    same_chars("coder", 1, 10)