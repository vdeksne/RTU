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


while True:
    try:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        if start > end:
            print("Start number must be smaller than end number!")
            continue
        break
    except ValueError:
        print("Both start and end numbers must be integers!")

cubes = []
for num in range(start, end+1):
    cube = num ** 3
    cubes.append(cube)
    print(f"{num} kubā: {cube}")

print("Visi kubi:", cubes)

# otra versija

# while True:
#     try:
#         start = int(input('Lūdzu ievadiet veselu sākuma skaitli: '))
#         end = int(input('Lūdzu ievadiet veselu beigu skaitli: '))
#         # could add more checks for start < end if you want
#         if start > end:
#             print('Sākuma skaitlim jābūt mazākam par beigu skaitli!')
#             continue # go back to start of loop
#         break
#     except ValueError:
#         print('Gan beigām gan sākumam jābūt veseliem skaitļiem!')


# visi_kubi = []
# # while x <= y:
# #     print(f'{x}  kubā: {x**3}')
# #     visi_kubi.append(x**3)
# #     x += 1

# # for loop would be more suitable since we know the range
# for i in range(start, end + 1):
#     print(f'{i}  kubā: {i**3}')
#     visi_kubi.append(i**3)
# # above is a fine approach

# # we could also do this with list comprehension
# # visi_kubi = [i**3 for i in range(start, end + 1)]
# # # now we print individual values using enumerate
# # for i, kubs in enumerate(visi_kubi, start=start):
# #     print(f'{i} kubā: {kubs}')

# print(f'Visi kubi: {visi_kubi}')
