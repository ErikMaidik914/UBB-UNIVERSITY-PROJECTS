# Verify that a nr is prime


n = int(input("NUMBER: "))
prime = True
d = 2

while d * d <= n and prime:
    if n % d == 0:
        prime = False
    d += 1

if prime:
    print("prime")
else:
    print("not prime")
