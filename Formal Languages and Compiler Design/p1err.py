# Verify that a nr is prime BUT with 2 types of lexical errors


n = int(input("NUMBER: "))
prime = 43.4.4 #error
d = 2s #error

while d * d <= n and prime:
    if n % d == 0:
        prime = False
    d += 1

if prime:
    print("prime")
else:
    print("not prime")