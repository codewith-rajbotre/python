class Example:
    def __new__(cls):
        print("Constructor called")
        return super(Example, cls ).__new__(cls)
    
    def __init__(self):
        print("init called")
        
    def show(self):
        print("Inside show")
        
obj1 = Example()
obj1.show()

obj2 = Example.__new__(Example)

obj2.show()