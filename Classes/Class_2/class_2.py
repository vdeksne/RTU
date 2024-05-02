#Uzrakstiet programmu, kas noprasa un saglabā lietotāja vārdu
#Uzdod jautājumu par lietotāja vecumu, jautājumā izmantojot lietotāja vārdu.
#Uzrāda pēc cik gadiem lietotājam būs 100 gadi :)
#BONUS: Lai programma uzrādā arī gadu kad lietotājam būs 100 gadi.

name = input("What's your name?")
print(f"Hello {name}!")
age = int (input(f"How old are you, {name}?"))
print(f"{age} ")
in_100_years = 100 - age
import datetime
current_year = datetime.datetime.now().year
year = current_year + in_100_years
print (f"In {in_100_years} years you will be 100 years old 🎉")

print (f"In {year} you will be 100 years old 🙌")

#Uzdod 3 jautājums par telpas platumu, garumu, augstumu
#Uzrāda cik liels būs telpas tilpums


width = float(input("Room's width (in meters)? "))
length = float(input("Room's length (in meters)? "))
height = float(input("Room's height (in meters)? "))
volume = str((length * width * height))
print("Room's volume is", volume, "m cubed")  


#Uzrakstiet programmu, kas noprasa temperatūru pēc Celsija un izdrukā šo temperatūru pēc Farenheita skalas.
#farenheit = 32+celsium*(9/5)
temp = float(input("Temperature in Celsius? "))
farenheit = 32 + temp*(9/5)
farenheit_rounded = round (farenheit, 2)
print(farenheit_rounded)