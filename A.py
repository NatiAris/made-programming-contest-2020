from itertools import count

x = int(input().strip())
ks = [int(input().strip()) for _ in range(x)]

desired_numbers = set(ks)
largest = max(desired_numbers)
acc = 1
results = {}
i = j = 0
for i in count():
    if acc > largest:
        break
    for j in range(i):
        if acc > largest:
            break
        if acc in desired_numbers:
            results[acc] = (2**i + 2**j) % 35184372089371
        acc += 1

for k in ks:
    print(results[k])
