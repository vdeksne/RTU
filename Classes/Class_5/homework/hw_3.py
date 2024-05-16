
# 3. Apgrieztie vārdi
# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.

sentence = input("Ievadiet teikumu: ")
words = sentence.split()
reversed_words = [word[::-1].capitalize() for word in words]
reversed_sentence = " ".join(reversed_words)
print(reversed_sentence)


# 4. Pirmskaitļi - šis varētu būt nedēļas nogales uzdevums, klasē diez vai pietiks laika
# Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam) pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Ievadiet cik pirmos pirmskaitļus gribat redzēt: "))
primes = []
num = 2
while len(primes) < n:
    if is_prime(num):
        primes.append(num)
    num += 1

print(primes)

# skaldi un valdi uzdevumus, lai būtu vieglāk pārskatāmi