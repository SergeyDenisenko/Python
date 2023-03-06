quantity = int(input('Введите количество элементов: '))
numbers = []

for i in range(1, quantity+1):
    numbers.append(int(input(f'Введите {i} элемент: ')))

numbers.sort()
print(numbers)