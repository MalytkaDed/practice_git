import os

a = ""
kol = int(input("колличество элементов в массиве: "))
print("массив: ")
mas = list(map(int, input().split()))
for i in range(kol - 1):
    a += str(mas[i]) + " "
a += str(mas[-1])

max_a = -10**10
k = 0
for i in range(0, len(a)):
    if a[i] == " ":
        max_a = max(max_a, int(a[k:i]))
        k = i+1
max_a = min(max_a, int(a[k: len(a)]))
print("минимальное число: ",max_a)
os.system("pause")
