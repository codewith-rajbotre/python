#Abstraction in Python

from abc import ABC, abstractmethod

print("Abstraction")

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass
    
class GooglePay(PaymentGateway):
    def pay(self):
        print("Paying using Google Pay.")
class PhonePe(PaymentGateway):
    def pay(self):
        print("Paying using Phone pe")
        
class Purchase:
    def __init__(self, gateway):
        self.gateway = gateway
        
    def checkout(self):
        print("Inside checkout method")
        self.gateway.pay()

p1 = Purchase(PhonePe())
p2 = Purchase(GooglePay())

p1.checkout()