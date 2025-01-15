print(bool('Kodnest')) # True
#print(int('Kod')) #Error
print(int('11')) #11
#print(float('Kodnest')) #Error
print(float('22.22')) #22.22
print(bool('')) #false
print(bool(0)) #false 
print(bool(12)) #True
#print(int('12.56')) #Error
print(int(12.56)) #12


#Taking float value from user and converting it into int
value = int(float(input('Enter price :Float value')))
print(value, type(value))
