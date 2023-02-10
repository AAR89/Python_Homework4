# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких 
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с
# двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед 
# некоторым кустом заданной во входном файле грядки.

n = int(input('Введите n: '))
tree = [int(i) for i in input('Введите количество ягод на кустах через пробел: ').split() ]
n = len(tree)
tree = tree + tree[:2]
max_berries = 0
for j in range(n):
    max_berries = max(max_berries,tree[j] + tree[j+1] + tree[j+2])
print(f'Максимальное количество собранных ягод - > {max_berries}')