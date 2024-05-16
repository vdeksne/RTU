# scripts so far 
#  for larger programs, we define functions 

# script for eating a sandwich"
# print("take two slices of bread")
# print("put some cheeese on the bread")
# print("put some tomato on the cheese")
# print("put two slices together")

# functions are defined with the def keyword, they can take arguments and return values, they are reusable

# def make_sandwich():
#     print("take two slices of bread")
#     print("put some cheeese on the bread")
#     print("put some tomato on the cheese")
#     print("put two slices together")

# make_sandwich()

# for i in range(5):
#     make_sandwich()


# def make_sandwich_with(filing):
#     print("take two slices of bread")
#     print("put some cheeese on the bread")
#     print(f"put some {filing} on the cheese")
#     print("put some cream-cheeese on the bread")
#     print("put two slices together")

# make_sandwich_with("ham", "[cucumber, beetroot, egg]")

# def make_sandwich_with(bread, filing):
#     print(f"take two slices of {bread}")
#     print("put some cheeese on the bread")
#     print(f"put some {filing} on the cheese")
#     print("put some cream-cheeese on the bread")
#     print("put two slices together")

# make_sandwich_with("rice", "ham")

def print_ad(a, b):
    print(f"{a} + {b} = {a + b}")

print_ad(2,3)

def add(a,b):
    return a + b

result = add(5, 6)
print(f"result is {result}")

def multiply(a,b):
    return a * b

result = multiply(5, 6)
print(f"result is {result}")

result = add(multiply(5,6), add(3,10))
print(f"result is {result}")


def get_int_input():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Please enter a number")  