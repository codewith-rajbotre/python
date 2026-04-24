class Demo:
    varBooks = "Python Tutorials"
    #Instance methods
    def __init__(self):
        print("init method")
    def config(self):
        print("Inside config method ")
        
    #Clas methods
    
    @classmethod
    def c_method(cls):
        return cls.varBooks;   
      
    #Static methods
    

    
d1 = Demo()

d1.config()
print(Demo.c_method())