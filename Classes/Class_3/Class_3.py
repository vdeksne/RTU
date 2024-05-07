
# collection
name="Vik"
for c in name: 
    # typical to use c for character
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

while user_input != "q":
    try:
        user_input = input("enter number or letter q and press enter")
        number = float(user_input)
        if user_input.lower().startswith("q"):
            print("okay")
    except ValueError:
        print("please enter e number!")
        continue
    total += number
    print("you entered", number)
    print("total is now", total)
