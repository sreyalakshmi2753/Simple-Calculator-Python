#MULTIPLICATION TABLE GENERATOR 

num = int(input("Enter the table: "))

print(f"\nMultiplication Table of {num}")
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")