# guess the number game

# Guess my number beteween 1 to 20 : 10
# 9 , your guess number is too high
# Guess my number beteween 1 to 20 : 5
# 9 , your guess number is too low
# Guess my number beteween 1 to 20 : 10
# Congrats, you guess my number in 3 attempts
import random
random.randint(1,20)
secnumber =random.randint(1,20)
print(secnumber)
a = int(input("Enter guess number :"))
if (a == secnumber):
    print("congrats you guessed the number")
elif (secnumber<a<20):
    print("guess number is too high")
elif (1<a<secnumber):
    print("guess number is too low")
        
