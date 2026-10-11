# 1: Define a list of numbers
listNum = [1, 2, 3, 4, 5, 8, 9, 10]

# 2. Using range(): Iterate through the list using indices and print each element with its index
print("Range:")
x = range(len(listNum))
for i in x:
    print(f"Index {i}: {listNum[i]}")

# 3: Using map(): Transform the list by squaring each number.
print("\nMap:\nSquared Numbers:")
def squarelist(n):
    return n * n

squaredList = list(map(squarelist, listNum))
for i in squaredList:
    print(i)

# 4: Using filter(): Extract and store only the even numbers from the list.
print("\nFilter Even Numbers:")
def even(n):
    return n % 2 == 0

evenList = list(filter(even, listNum))
print(evenList)

# 5: Using zip(): Pair each original number with its squared value
print("\nZip:")
z = zip(listNum, squaredList)
for listNum, squaredList in z:
    print(f"{listNum} squared is {squaredList}")