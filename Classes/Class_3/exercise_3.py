# 1. FizzBuzz
# Izdrukāt virknīti 1,2,3,4,Fizz,6,Buzz,8,.....34,FizzBuzz,36,....līdz  97,Buzz, 99,Fizz 
# Tātad ja skaitlis dalās ar 5 tad Fizz
# Ja dalās ar 7 tad Buzz,
# Ja dalās ar 5 UN 7 tad Fizzbuzz
# savādāk pats skaitlis
# Piezīme: šads uzdevums kļuva populārs kā pirmais uzdevums, ko uzdot, lai noteiktu vai cilvēks vispār zina par programmēšanu :)

for i in range(1, 100):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)

# 2. Eglīte
# Ievadiet eglītes augstumu
# Izdrukājiet eglīti:
# Piem. augstums == 3
# Izdruka būtu:
#   *
#  ***
# *****
# Piezīme: atceramies, ka vairākus simbolus var izdrukāt piemēram šādi: print(" "*10+"*"*6) 

# Iegūst eglītes augstumu no lietotāja
height = int(input("Ievadiet eglītes augstumu: "))

# Cikls, kas izveido eglīti
for i in range(height):
    # Izdrukā tukšās vietas (lai centrētu zvaigznītes)
    print(" " * (height - i - 1) + "*" * (2 * i + 1))

# 3. Pirmskaitlis
# Atrodiet vai ievadītais veselais pozitīvais skaitlis ir pirmskaitlis.
# Pirmskaitlis ir skaitlis, kas dalās bez atlikuma tikai pats ar sevi un 1.
# Piezīme: šo uzdevumu var sākt risināt ļoti vienkārši un varat arī pēc tam optimizēt. 
# (kaut vai tas, ka mums nav jāpārbauda dalīšanās ar skaitļiem, kas lielāki par ievadītā skaitļa kvadrātsakni)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Iegūst skaitli no lietotāja un pārbauda, vai tas ir pirmskaitlis
number = int(input("Ievadiet veselu skaitli: "))
if is_prime(number):
    print(f"{number} ir pirmskaitlis.")
else:
    print(f"{number} nav pirmskaitlis.")

# optimizētāk: 


import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 un 3 ir pirmskaitļi
    if n % 2 == 0 or n % 3 == 0:
        return False  # Izslēdz visus pāra skaitļus un skaitļus, kas dalās ar 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Iegūst skaitli no lietotāja un pārbauda, vai tas ir pirmskaitlis
number = int(input("Ievadiet veselu skaitli: "))
if is_prime(number):
    print(f"{number} ir pirmskaitlis.")
else:
    print(f"{number} nav pirmskaitlis.")
