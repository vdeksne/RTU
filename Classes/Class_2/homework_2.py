# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
# Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
# Ja ir pāri 37, tad izvadiet "iespējams drudzis"

print ("alus " *3)

food=1

print (type("food"))


temperature = float (input("What's your temperature?"))

if temperature < 35:
     print("nav par aukstu")
elif temperature > 37:
    print("iespējams drudzis")
else:
    print("viss kārtībā")


#  2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem. 

# Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.

salary = int(input("What's your salary?"))
seniority = int(input("How many years have you worked for your company?"))
bonus = int(salary * 0.15 * (seniority-2))


# Izvadiet bonusu.

if seniority <= 2:
     print("better luck next year")
else:
    print("Your bonus this year is ", bonus)


# Piemērs 5 gadu stāžs, 1000 Eiro alga, bonuss būs 450 Eiro.

# 3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā. // sakārtoti dilstošā secībā 

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
c = int(input("Enter the third number "))


# Sort the numbers using nested if-elif-else based on the description
if a > b and a > c:  # a is the largest
    if b > c:
        print(a, b, c)  # a, b, c
    else:
        print(a, c, b)  # a, c, b
elif b > a and b > c:  # b is the largest
    if a > c:
        print(b, a, c)  # b, a, c
    else:
        print(b, c, a)  # b, c, a
else:  # c must be the largest
    if a > b:
        print(c, a, b)  # c, a, b
    else:
        print(c, b, a)  # c, b, a


# Piezīme: pagaidām šo uzdevumu risinam tikai ar if, elif, else darbībām

# Pastāv arī risinājums izmantojot kārtošanu un list struktūru, kuru vēl neesam skatījuši.
