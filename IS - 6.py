import random
def main():
# Step 1: Agree on a prime number (p) and a base number (g)
p = get_prime(512)
g = 2
# Step 2: Alice generates a random number (a) and computes A = g^a mod p
a = random.randint(2, p-2)
A = pow(g, a, p)
# Step 3: Bob generates a random number (b) and computes B = g^b mod p
b = random.randint(2, p-2)
B = pow(g, b, p)
# Step 4: Both Alice and Bob compute the shared secret key (K)
K1 = pow(B, a, p)
K2 = pow(A, b, p)
# Check if both keys are the same
if K1 == K2:
print("Shared Secret Key: " + hex(K1)[2:])
else:
print("Error: Keys do not match")
def get_prime(bits):
while True:
p = random.getrandbits(bits)
if is_prime(p):
return p
def is_prime(n, k=20):
if n <= 1:
return False
if n <= 3:
return True
if n % 2 == 0:
return False
# Write n as 2^r * d + 1
r, d = 0, n - 1
while d % 2 == 0:
r += 1
d //= 2
# Witness loop
for _ in range(k):
a = random.randint(2, n - 2)
x = pow(a, d, n)
if x == 1 or x == n - 1:
continue
for _ in range(r - 1):
x = pow(x, 2, n)
if x == n - 1:
break
else:
return False
return True
if __name__ == "__main__":
main()
