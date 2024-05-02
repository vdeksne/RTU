# 1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru.
# Ja lietotājs ievada zem 35, tad prasiet vai "nav par aukstu"
# Ja no 35 līdz 37 (ieskaitot), izvadiet "viss kārtībā"
# Ja ir pāri 37, tad izvadiet "iespējams drudzis"


temprature = float (input("What's your temperature?"))

if temprature < 35:
     print("nav par aukstu")
elif temprature > 37:
    print("iespējams drudzis")
else:
    print("viss kārtībā")


#  2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.

# Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.

# Izvadiet bonusu.

# Piemērs 5 gadu stāžs, 1000 Eiro alga, bonuss būs 450 Eiro.

# 3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā.

# Piezīme: pagaidām šo uzdevumu risinam tikai ar if, elif, else darbībām

# Pastāv arī risinājums izmantojot kārtošanu un list struktūru, kuru vēl neesam skatījuši.
