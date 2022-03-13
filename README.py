import random
# пока длина массива не будет 10 (продолжать цикл)
l = []
tmp = int(input("Введите длмну массива"))
while len(l) != tmp:
    num = random.randint(10, 99)
    if num %2 == 0:
        l.append(num)
print(l)
