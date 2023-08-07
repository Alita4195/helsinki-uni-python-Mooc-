class Animals:
    def eat(self, food:str): #self 是实例对象，是经过Class 实例化获得的，比如dog=Animal()#这里的dog就是一个实例对象。
        
        print("eating", food)
    def play(self):
        print("Gaming...")
    def sleep(self):
        print("zzz...")
        
#Animals.play(self) #NameError: name 'self' is not defined, 是因为这个变量没有赋值
dog=Animals()
Animals.play(dog) #works


