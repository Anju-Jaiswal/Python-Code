'''
1. In List we can store Homogeneous as well as Heterogeneous Data.
2. In List we can store Duplicate Values.
3. Lis is an Ordered Collection of Data: Order of insertion  will as 
   it in th output.
4. Lists are Mutable : Once we declare the list we can modify it.
'''

li1 = [10, 20, 44.45, True, 'Kodnest']
print(li1, type(li1))

#appened(): will add element at the end of List.
li1.append(20)
print(li1) #[10, 20, 44.45, True, 'Kodnest',20]

li1.insert(1,15)
print(li1) #[10, 15, 20, 44.45, True, 'Kodnest',20]

#remove(arg): Remove first occurrence of the specific element.
li1.remove(20)
print(li1)

#in and not in Operator:
print(2000 in li1)#false
print('Kodnest' in li1)#true

#pop(): Without argument will delete and return last element from list
removed_ele = li1.pop()
print(removed_ele)#20
print(li1)#[10, 15, 44.45, True, 'Kodnest']

#pop(): With argument will delete the element at specified index
removed_ele = li1.pop(3)
print(removed_ele) #True
print(li1) #[10, 15, 44.45, 'Kodnest']

#del keyword:
del li1[1]
print(li1) #[10, 44.45, 'Kodnest']

del li1
print(li1) #error : name 'li1' is not defined