# Display and Count Number from 1 to 9
even = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        even += 1
print(f"We have {even} even numbers")
