# Write your solution here
def formatted(my_list):
    results = []
    for item in my_list:
        item=f"{item:.2f}"
        results.append(item)
    return (results)
        
if __name__=='__main__':
    formatted([1.234, 0.3333, 0.11111, 3.446, 1.23])