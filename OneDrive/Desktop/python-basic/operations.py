# arithmeatic operations
print("Addition: " , 5 + 3)
print("Subtraction: " , 5 - 3)
print("Multiplication: " , 5 * 3)
print("Division: " , 5 / 3)
print("Floor Division: " , 5 // 3)
print("remainder: " , 5 % 3) # modulo => remainder
print("exponent: " , 5 ** 3) # 5^3 = 5*5*5


# shortcuts => assignment operators
x = 10
x += 5 # x = x + 5
x -= 5 # x = x - 5
x *= 5 # x = x * 5
x /= 5 # x = x / 5  
x//= 3 # x = x // 3
x**= 5 # x = x ** 5
x%= 3 # x = x % 3


#comparison operators
# <, >, <=, >=, ==, !=
print(5 < 3) # False
print(5 > 3) # True
print(5 <= 3) # False
print(5 >= 3) # True
print(5 == 3) # False
print(5 != 3) # True

# logical operators
# and, or, not
stt1 = 3 > 5
stt2 = 3 > 2
print(stt1 or stt2) # True
print(stt1 and stt2) # false
print((3>4) or (3>1)) # True
print((3>4) and (3>1)) # False
print(not (3>4)) # True
print(not True) # False
print(not False) # True
print(not stt1) # True 