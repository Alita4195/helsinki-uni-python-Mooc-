# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name:str, weight:int):
        self.name=name
        self.weight=weight
    def __str__(self):
        return f"Present: {self.name} ({self.weight}kg)"

class Box:
    def __init__(self):
        self.present_list = []  
        self.weights = 0   

    def add_present(self, present: Present):
        self.present_list.append(present.name)
        self.weights += present.weight
        return self.present_list, self.weights

    def total_weight(self):
        return (add_present(self, present)[1])
        
# class Box:
#     def __init__(self):
#         self.present_list = []  
#         self.weights = 0   

#     def add_present(self, present: Present):
#         self.present_list.append(present.name)
#         self.weights += present.weight
#         return self.present_list

#     def total_weight(self):
#         return self.weights

if __name__ == "__main__":
    #box=Box()
    #print (box.add_present(Present("Ball",1))) functional 


    present_list=[]
    weight_sum=0    
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
