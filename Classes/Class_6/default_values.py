
def greet_person(name, greeting):
    print(f"{greeting} {name}")

def greet_person_with_default(name="Jo", greeting="Hello"):
    print(f"{greeting} {name}")

greet_person_with_default("Vik")
greet_person_with_default("Vik", "Hi")
greet_person_with_default()

print("vika", "nik", "jo", sep="|X|",end="!\n")

def eat_meal(*ingredients, drik="water"):
    print("I am eating a meal with:")
    for ingredient in ingredients:
        print(ingredient)
    print(f"and drinking {drik}")

eat_meal("bread", "cheese", "ham", "tomato", drik="juice")