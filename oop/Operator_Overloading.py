# a = '5'
# b = '6'

# a = 5
# b = 6

# c = a + b

# c = int.__add__(a, b)

# print(c)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return f'{self.name} : {self.balance}'
    #operator overloading
    def __add__(self, other):
        return Account('combined', self.balance + other.balance)
        
        
user1 = Account('user11', 1000)
user2 = Account('user22', 3000)

print(user1)
print(user2)

combined = user1 + user2
print(combined)