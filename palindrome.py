'''wap to check if number is palindrome'''
num = int(input("Enter a palindrome :"))
#print("num = ",num)
b = num
rev = 0
while(num>0):
    rem =num%10
    rev=rev*10+rem
    num=num//10

print(rev)
print(num)
if(rev == b):
    print("num is palindrome")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
