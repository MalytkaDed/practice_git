import os
a = input()
max_a = -10**10
k = 0
for i in range(0, len(a)):
    if a[i] == " ":
        max_a = max(max_a, int(a[k:i]))
        k = i+1
max_a = max(max_a, int(a[k: len(a)]))
print(max_a)
os.system("pause")
