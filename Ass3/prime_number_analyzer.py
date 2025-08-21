start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

with open("primes.txt", "w") as file:
    for num in range(start, end + 1):
        if is_prime(num):
            file.write(str(num) + "\n")
