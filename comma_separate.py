'''wap to read a no. 1 to n and print sum of all the no.s'''
n = int(input("Enter last no. : "))
s = 0
for i in range(1,n+1):
    print(i)
    s = s + i
    
print(s)
