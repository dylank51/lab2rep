lst = []
numbers = int(input('Amount of numbers:  '))

for n in range(numbers):
    num = int(input('Enter number '))
    lst.append(num)

print('Maximum element in the list is :', max(lst))


