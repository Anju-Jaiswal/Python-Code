for i in 'Kodnest':
    print(i)

for j in [10,20,30]:
    print(j+5)

for num in range(1, 10):
    print(num)

for num in range(11,21,2):
    print(num, end=" ")

print()

for i in range(1,11):
    if(i % 2 == 0):
        print(i)

i = 0   
while(i<10):
    print(i+100)
    i = i+1
print('________________________')

for i in range(1,10):
    if(i==6):
        continue
    print(i)
print('________________________')

for i in range(1,10):
    if(i==5):
        break
    print(i)

def disp():
    pass
disp()
    