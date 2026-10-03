time ="dinner"
place = "anna chinese corner"
cost = 6543
service_charge = 0.15 * cost
size = 3
total = cost + service_charge
split = total / size

print("")
print("welcome to payup")
print("")
print(f"here's the breakdown for {time} at {place} ")
print("")
print(f"cost: ${cost}")
print(f"service charge: ${service_charge}")
print(f"group size: {size}")
print(f"Grand total: ${total}")
print("")
print(f"each person must payup: ${split}")
print("")
print("")