i = 1
while i < 6:
    print(i)
    i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
