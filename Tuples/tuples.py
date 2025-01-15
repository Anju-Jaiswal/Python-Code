'''
In tuple we can store Homogeneous as well as Heterogenous Data.
Tuples can store duplicates value
Tuples are ordered collection of data
Tuples are immutable means once we declared the tuple we can not modify it
'''
tup1 = (10, 22.5, 'Kodnest', True, 10)
print(tup1)#(10, 22.5, 'Kodnest', True, 10)

print(tup1[2]) #"Kodnest"

#Deletes the complete tup1 object
del tup1
#print(tup1[2]) #error

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)