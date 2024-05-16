
# 3. Apgrieztie vārdi
# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.

sentence = input("Ievadiet teikumu: ")
words = sentence.split()
reversed_words = [word[::-1] for word in words]
reversed_sentence = " ".join(reversed_words)
print(reversed_sentence)


# 4. Pirmskaitļi - šis varētu būt nedēļas nogales uzdevums, klasē diez vai pietiks laika
# Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam) pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]