# Write your solution here
def factorials(n: int):
    k={}
    if n<=0:
        k[n]=1
        return(k)
    else:
        result=1
        for n in range(1, n+1):
            result=result*n
            k[n]=result
        return (k)    

if __name__ == "__main__":
    factorials(5)