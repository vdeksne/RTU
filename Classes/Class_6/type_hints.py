def add(a:int, b: int) -> int:
    return a + b

print(add(5, 6))

print(add("viktors", "deksnis"))

print(add(5.3434, 6.6766))
def sum_list(input_list: list[int], greeting: str ="Let's rock!") -> int:
    print(greeting)
    return sum(input_list)

print(sum_list([1,2,3,4,5,6,7,8,9,10]))
print(sum_list([1,2.4,3,4,5]))