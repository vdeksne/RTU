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