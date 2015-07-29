# Counter
# Demonstrates the range() function
s = 0
print("Counting:")
for i in range(10):
    print(i, end=" ")

print("\n\nCounting by fours:")
for i in range(2, 100, 4):
    s = s + 1
    print(i, end=" ")
    print(s)

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nPress the enter key to exit.\n")
