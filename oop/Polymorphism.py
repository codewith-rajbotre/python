class Laptop:
    def build(self):
        print("From laptop build function")
        
class Desktop:
    def build(self):
        print("Inside desktop build file")

class Comp:
    def code(self, machine):
        print("Code from comp building")
        machine.build()

asus_rog = Laptop()

acer_desk = Desktop()

user = Comp()

# user.code(asus_rog)

user.code(acer_desk)