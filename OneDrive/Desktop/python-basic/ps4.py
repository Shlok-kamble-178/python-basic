for i in range(1, 21):
    if i % 2 == 1:
        print(i)

for i in range(1, 20, 2):

    print(i)

a = int(input("Enter a number: "))
for i in range(1, 11):
    print(i * a)

for i in range(1, 50):
    if (i == 15):
        continue
    if i % 3 == 0:
        print(i)


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
for i in range(1, 1000):
    if i % a == 0 and i % b == 0:
        print(i)
