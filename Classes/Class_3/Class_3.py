
# # collection
# name="Vik"
# for c in name: 
#     # typical to use c for character
#     print("working with letter", c)

# my_emoji = "👨‍🎓👩‍🎓🤓🎓🏫✍️👨‍💻👨‍💼👩‍💼🧑‍💻🧑‍💼👩‍💻📚🎒"
# for emoji in my_emoji:
#     print ("Emji", emoji, "unicode number", ord(emoji))

#     for i, c in enumerate(name):
#         print(f"No.{i} -> symbol {c} -> its unicode {ord(c)}")

# for i in range(10):
#     print(i)
#     if i == 4:
#         print("i is 4?", i)
#         break
# else:
#     print("finished for loop normally")

# total = 0 

# while user_input != "q":
#     try:
#         user_input = input("enter number or letter q and press enter")
#         number = float(user_input)
#         if user_input.lower().startswith("q"):
#             print("okay")
#     except ValueError:
#         print("please enter e number!")
#         continue
#     total += number
#     print("you entered", number)
#     print("total is now", total)

    # New notes start here 

    # CIKLI 

# print("Hello")
    
# while True:
#     print("Hello")

# condition

i = 5
while i < 5:
    print("i is now", 1)
    i+=1
print("i will be", i)

floor = 9
while floor > 0:
    print(f"Going down to floor {floor}")
    floor -= 1
print(f"whew, we are finally on floor {floor}")

# different size steps
cnt = 10
while cnt < 20:
    print(f"Cnt is now {cnt}")
    cnt += 2
print(f"after while loop ends cnt {cnt}")

i = 0 
total = 0 
while i < 1000:
    total += i #gauss
    #show updates every 100
    if i % 200 == 0:
        print(f"iteration No. {i} total is now {total}")
    i+=1
print(f"Final total {total}, iteration {i}")

# generalized
start = 100
stop = 200
step = 25
i = start 
while i < stop: 
    print(f"doing something with {i}")
    i += step
print(f"all done, i is now {i}")

i = 0
while i < 10:
    print("i is", i)
    i +=1
    if i > 5:
        print("time to break early")
        break
    print("still inside loop", i)
print("all done, i is", i)

i = 0
import random
while i < 10_000:
    dice_throw = random.randint(1,6)
    if dice_throw == 6:
        print("nice 6 you have", dice_throw)
        print("breaking free on iteration", i)
        break
    i+=1
print("we are free")

i = 9000

# we can use while true with break 
while True: 
    # print("running forever or am I?")
    if i % 1_000_000 == 0:
        print("i is ", i)
    if i > 4:
        print("Breaking free", i)
        break
    i+=1
# free
print("after break i is", i)

