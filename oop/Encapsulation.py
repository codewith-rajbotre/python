class Bank:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance

b1 = Bank(555)

b11= b1.get_balance()
print(b11)