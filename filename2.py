""" Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""
f_name = input("Enter filename :" )
print(f_name)
length_of_f_name=len(f_name)
for i in range(length_of_f_name):
    print()
    print(f_name[i])

for i in range(length_of_f_name):
    if(f_name[i] == '.'):
        print(f_name[i])
        location = i
print("====")


print("location : ",location)
print("length of file name : ", length_of_f_name)

new_fname = []
j = 0
for i in range(location, length_of_f_name):
    print(f_name[i])
    new_fname.append(f_name[i])
    #new_fname[j] = f_name[i]
    print(j)
    j += 1
    
print(new_fname)

new_var = ''

for i in range(len(new_fname)):
    print(new_fname[i])
    new_var = new_var + new_fname[i]
    
print(new_var)
