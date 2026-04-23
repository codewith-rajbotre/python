#Set example

set1 ={1,2,3,4}

print(set1)
print(type(set1))

#Decleration of empty set

set2 = {}  # it creates a empty dictionary not an empty set
print(set2)
print(type(set2))

# to create a empty set use a set() method
set3 = set()
print(set3)
print(type(set3))

#Frozen Set 

set4 = frozenset([33,22,11])
print(type(set4))

#we can insert forzen set inside the another set
set5 = {11, 12,set4}
print(set5)

#we could not directly insert an set into an another set
#set6= {11, 12, set1}
#print(set6)

#for inserting set into another set firstly we have to convert set into frozenset and then merge into another set

set7 = {11, 12, frozenset(set1)}
print(set7)