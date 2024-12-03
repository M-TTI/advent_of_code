left = []
right = []
tot = 0
sim = 0
with open('day1_input.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        a = [int(i) for i in line.split()]
        left.append(a[0])
        right.append(a[1])
    file.close()

# Part 1
for i in range(len(left)):
    l = left.index(min(left))
    r = right.index(min(right))
    tot += abs(int(left[l]) - int(right[r]))
    left.pop(l)
    right.pop(r)

print(f'total distance = {tot}')

with open('day1_input.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        a = [int(i) for i in line.split()]
        left.append(a[0])
        right.append(a[1])
    file.close()

# Part 2
for i in left:
    c = 0
    for j in right:
        if i == j:
            c += 1
    sim += i * c

print(f'similarity score = {sim}')
