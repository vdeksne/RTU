# infinite loop break and continue
i = 0
is_end_of_world = False
while i < 4 and not is_end_of_world:
    my_input = input("Enter number or q to quit: ")
    if my_input == "q":
        break
    num = float(my_input)
    print(num, "cubed is", round(num**3, 2))
    if num**3 > 9000:
        print("Big result!")
        is_end_of_world = True
    i += 1
print("This will will print after break")