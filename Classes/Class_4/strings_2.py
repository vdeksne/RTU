print("fun with python")

#  stringi - teksta virknes

food = "potatoe"
print(f"{food=}")
drink = "milk"
print(food[1])#we start with 0 
print(food[0])
print(len(food))
print(food[len(food)-1])
print(food[-1])
for c in food:
    print(c, end=" :: ")
print(food[3:])
print(food, food[::2])
my_food = "kartupelis"
print(my_food, my_food[3:8:2])
print(my_food, my_food[::-1])#pythonic way of reversing string 

print(my_food.find("p"))#finds the first occurence of the substring
#my_food[5] = "m" #stringi ir immutable
new_food = my_food.replace("p", "m")#to change strings we need to make new ones 
print(new_food)
another_food = my_food[:5] + "m" + my_food[6:]
print(another_food)
full_food = "liels " + my_food
print(full_food)
full_food.count("l")
print("k" in full_food) #in checks if the substring is in the string, boolean result
count = 0 
for c in full_food:
    if c == "l":
        count += 1
    print(f"Letter l can be found {count=}")
    print("Valdis" > "Voldermars")
    print("a" > "o")
    print(ord("a"), ord("o"), ord("ā"))
 
