str = "This is a cat"
vowel = "aeiou"

count = 0

for item in str:
    if item in vowel:
        print(item)
        count+=1

print(count)
