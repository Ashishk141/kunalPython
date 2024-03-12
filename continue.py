# Simple Python program with continue statement

# Define a range (e.g., 1 to 10)
start_range = 1
end_range = 10

print("Printing odd numbers in the range {} to {}:".format(start_range, end_range))

# Loop through the range and print odd numbers
for number in range(start_range, end_range + 1):
    # Check if the number is even
    if number % 2 == 0:
        # Skip even numbers using continue statement
        #break
        continue
        #print("")
    # Print odd numbers
    print(number)

    

print("End of program.")
