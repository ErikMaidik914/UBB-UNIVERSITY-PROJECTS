# Displays the minimum

x = int(input("FIRST: "))
y = int(input("SECOND: "))
z = int(input("THIRD: "))


Min = x
if y < Min:
    Min = y
if z < Min:
    Min = z

print(Min)
