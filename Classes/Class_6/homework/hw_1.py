# 1.a Vidējā vērtība
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.

numbers = []
while True:
    number = input("Ievadiet skaitli (q, lai izietu): ")
    if number == "q":
        break
    numbers.append(float(number))
    average = sum(numbers) / len(numbers)
    print("Vidējā vērtība:", average)

# 1.b
numbers = []
while True:
    number = input("Ievadiet skaitli (q, lai izietu): ")
    if number == "q":
        break
    numbers.append(float(number))
    average = sum(numbers) / len(numbers)
    print("Visi ievadītie skaitļi:", numbers)
    print("Vidējā vērtība:", average)

# 1.c
numbers = []
while True:
    number = input("Ievadiet skaitli (q, lai izietu): ")
    if number == "q":
        break
    numbers.append(float(number))
    average = sum(numbers) / len(numbers)
    top3 = sorted(numbers)[-3:]
    bottom3 = sorted(numbers)[:3]
    print("TOP3 skaitļi:", top3)
    print("BOTTOM3 skaitļi:", bottom3)
    print("Vidējā vērtība:", average)

# optimizēts:

skaitli = []
 
while True:
    ievade = input("Ievadiet skaitli (vai 'q' lai izietu): ")
    if ievade.lower() == 'q':
        break
    try:
        skaitls = float(ievade)
        skaitli.append(skaitls)
        videja_vertiba = sum(skaitli) / len(skaitli)
        print("Visi skaitļi:", skaitli)
        print("Vidējā vērtība:", videja_vertiba)
    except ValueError:
        print("Ievadiet derīgu skaitli!")



# 2. Kubu tabula
# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
# Izvads ir ievadītie skaitļi un to kubi
# Piemēram: ievads 2 un 5 (divi ievadi)
# Izvads 
# 2 kubā: 8
# 3 kubā: 27
# 4 kubā: 64
# 5 kubā: 125
# Visi kubi: [8,27,64,125]
# PS teoretiski varētu iztikt bez list, bet ar list būs ērtāk

# 3. Apgrieztie vārdi
# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.


# 4. Pirmskaitļi - šis varētu būt nedēļas nogales uzdevums, klasē diez vai pietiks laika
# Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam) pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]