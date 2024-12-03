left = []
right = []
tot = 0
with open('day1_input.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        a = [int(i) for i in line.split()]
        left.append(a[0])
        right.append(a[1])

for i in range(len(left)):
    l = left.index(min(left))
    r = right.index(min(right))
    tot += abs(int(left[l]) - int(right[r]))
    print(f'{i} : {abs(int(left[l]) - int(right[r]))}')
    left.pop(l)
    right.pop(r)

print(tot)
