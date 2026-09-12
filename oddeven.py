num = int(input("Enter a number: "))

odd = [x for x in range(1, num) if x % 2 != 0]
even = [x for x in range(1, num) if x % 2 == 0]

print("Odd numbers:", odd)
print("Even numbers:", even)