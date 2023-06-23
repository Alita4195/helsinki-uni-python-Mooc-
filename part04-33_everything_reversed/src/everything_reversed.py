# Write your solution here
def everything_reversed(my_list:list):
    reverse_item=[]
    my_list=reversed(my_list)
    for item in my_list:
        item=item[::-1]
        reverse_item.append(item)
    return (reverse_item)
if __name__ == "__main__":
    everything_reversed(["Hi", "there", "example", "one more"])