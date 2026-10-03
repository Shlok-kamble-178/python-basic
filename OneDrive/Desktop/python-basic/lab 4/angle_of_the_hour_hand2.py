# sir's expectation

h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter second: "))

h_angle = 30 * h
m_angle = 1/2 * m
s_angle = 1/120 * s
total_angle = h_angle + m_angle + s_angle

if total_angle > 360:
    total_angle = total_angle - 360

print(f"the angle is {total_angle}")

"""
here we tried to reduced the code just by trying to use only one print fxn.
sir's expectation
"""