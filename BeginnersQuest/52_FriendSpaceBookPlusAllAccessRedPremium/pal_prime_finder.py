def is_palindrome(n:str):
    for i in range(len(n)//2):
        if n[i] != n[-(i+1)]:
            return False
    return True

with open("/root/Downloads/2T_part1.txt", "r") as primes:
    with open("palprimes.txt", "w") as palprimes:
        for line in primes.readlines():
            numbers = line.split()
            for n in numbers:
                if is_palindrome(n):
                    palprimes.write("{}\n".format(n))

