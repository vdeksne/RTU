    # we ensure user input is valid 
    # combine try except with while loop 

#catch errors:
while True: 
    try:
        num = int(input("please enter an integer"))
        print(f"thank you square of {num is {num**2}}")
        break
    except ValueError:
        print("you did not enter valid integer")
        print("try another number")
    print("reset of program starts")
    print ("num is value", num, "and its type is", type(num))

    