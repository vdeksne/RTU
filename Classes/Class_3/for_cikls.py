# konkrētam skaitam ir for cikls 

# for i in range(5):
#     print(i is i, i)
# print("outside i is now", i)

# for i in range(10,15):
#     print(i is i, i)
# print("outside i is now", i) 

# for i in range(30,50,2): #lēciens pa divi
#     print(i is i, i)
# print("outside i is now", i) 

# for i in range(100,90, -2):
#     print(i is i, i)
# print("outside i is now", i) 
#
# NumPy external library

# STRINGI
# kolekcija/ virkne ar burtiem:

name="Vik"
for c in name: 
    # typical to use c for character as in Collection
    print("working with letter", c)

my_emoji = "👨‍🎓👩‍🎓🤓🎓🏫✍️👨‍💻👨‍💼👩‍💼🧑‍💻🧑‍💼👩‍💻📚🎒"
for emoji in my_emoji:
    print ("Emji", emoji, "unicode number", ord(emoji))

    for i, c in enumerate(name):
        print(f"No.{i} -> symbol {c} -> its unicode {ord(c)}")

for i in range(10):
    print(i)
    if i == 4:
        print("i is 4?", i)
        break
else:
    print("finished for loop normally")



total = 0 
user_input = ""

while user_input != "q":
    try:
        user_input = input("enter number or letter q and press enter ")
        number = float(user_input)
        if user_input.lower().startswith("q"):#works for Quit, q...
            print("okay")
        total += number
        print("you entered", number)
        print("total is now", total)
    except ValueError:
        # if user_input != "q":
        print("please enter e number!")
        continue
   

