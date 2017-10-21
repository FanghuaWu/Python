#i = 0
#numbers = []
#
#while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)
#
#    i = i + 1
#    print("Numbers now:", numbers)
#    print(f"At the bottom i is {i}")

def func_numbers(numb):
    i = 0
    numb = []

    print("Please input the maximum value: ")
    count = input("> ")

    print("Please input the loop step: ")
    step = input("> ")
    
    for i in range(0,int(count),int(step)):
       print(f"At the top i is {i}")
       numb.append(i)
   
       print("Numbers now:", numb)
       print(f"At the bottom i is {i}")

    return numb

numb = []
numbers = func_numbers(numb)

print("The numbers: ")
print(numbers)

for num in numbers:
    print(num)
