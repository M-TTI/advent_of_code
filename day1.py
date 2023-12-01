stringf = ''


def sum_digits(string):
    l = ''
    somme = 0
    split = string.splitlines()
    for i in split:
        for j in i:
            if j.isnumeric():
                l += j
        if len(l) == 1:
            nb = 2*l
        else:
            nb = l[0] + l[-1]
        l = ''
        somme += int(nb)
    return somme


def sum_numbers(string):



with open("day1_data", "r") as file:
    for line in file:
        stringf += line

print(sum_digits(stringf))