# lai nerakstītu 

# print("hello")
# print("hello")
# print("hello")
# my_string = "Hello, World!"
# print(my_string)
# izmantojam ciklus
#  likeam mainīgo I iteratoru 

# i = 0
# while i < 5:
#     print("hello no.1,", i)
#     i += 1
# print("always happens once loop is finished")
# print("i is now", i)
# i = 10
# while i > 0:
#     print("going down the floor:", i)
#     i -= 2
# print("whew, we are done with this i:" i)


# Do while loop īpašība is that the loop runs at least once before checking the condition.


# i = 20 
# while True:
#     print("i is", i)
#     if i > 28:
#         break
#     i += 2 

# while True:
#     res = input("enter a number or q to quit")
#     if res == "q":
#         print("no more calculatons today")
#         break 
#     elif res == "a":
#         print("I can't cube this")
#         continue
#     num = float(res)
#     print(f"my calculator says cube of {num} is {num**3}")

# print("all done whew!")    

#  for loops are used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal. 
   
for n in range(5):
    print("number is:", n)
print("done with the loop")
for n in range(2, 5):
    print(n)
for my_num in range(100, 110,2): #i can add step to range 
    print(my_num)
my_name = "Vik"
for c in my_name:
    print("letter,",c)

my_list = [1,2,100,105,"vik", "potatoes", 9000]
total = 0
big_items = 0 
for item in my_list:
    print("working with item: ", item)
    if type(item) == int or type(item) == float:
        total += item
        if item > 100:
            big_items += 1

my_num_list = [1,6,17,-6,49,642,6,2]
my_max = None
for num in my_num_list:
    if my_max == None:
        my_max = num
    if num > my_max:
        my__max = num
        
print(max(*my_num_list))



    
