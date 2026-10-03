# my work

h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter second: "))

if 0 <= h < 12 and 0 <= m < 60 and 0 <= s < 60:
    h_angle = 30 * h
    m_angle = 1/2 * m
    s_angle = 1/120 * s
    total_angle = h_angle + m_angle + s_angle
    print(f"The angle is {total_angle}")
else:
    print(("Error"))
