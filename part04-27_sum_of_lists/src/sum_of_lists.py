# Write your solution here
def list_sum(a:list, b:list):
    index=0
    list_sum=[]
    while index<len(b):
            
            list_sum.append(a[index]+b[index])
            index+=1
    return(list_sum)


if __name__=='__main__':
    a = [1, 2, 3]
    b = [7, 8, 9]
    list_sum(a, b)

