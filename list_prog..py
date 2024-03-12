# write a program to get the number as input and store multiple value in the list
lst = []
b = int(input("number of times u want to enter"))

for a in range(b):
  a = int(input("enter a number : "))
  if (a%2==0):
     lst.append(a)
  else:
    print("input even number")
  #print(a)
#lst.append(a)
print(lst)

"""
minimum requir.
jitna baar chlana h usk liye forloop
we can store multiple values
user s input

"""
