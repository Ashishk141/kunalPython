'''wap to print the sum of even no.s'''
n = int(input("Enter nth number :"))
s = 0
for i in range(0, n+1,2):
    print(i)
    s = s+i
print("sum of evne number: ",s)
