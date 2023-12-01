stringf = []


def sum_digits(string):
    l = ''
    somme = 0
    for i in string:
        for j in i:
            if j.isnumeric():
                l += j
        if len(l) == 1:
            nb = 2*l
        else:
            nb = l[0] + l[-1]
        l = ''
        print(nb)
        somme += int(nb)
    return somme


def sum_numbers(string):
    corrected_string = []
    digits_string = []
    digits = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9", "ten" : "10"}
    errors = {"oneight" : "oneeight", "twone" : "twoone", "treeight": "threeeight", "fiveight": "fiveeight", "sevenine" : "sevennine", "eightwo": "eighttwo", "eighten": "eightten", "nineight": "nineeight", "tenine" : "tennine"}
    for i in string:
        for j,k in errors.items():
            i = i.replace(j,k)
        corrected_string.append(i)
    for i in corrected_string:
        for j,k in digits.items():
            i = i.replace(j,k)
        digits_string.append(i)
    return digits_string


with open("day1_data", "r") as file:
    for line in file:
        stringf.append(line)

print(sum_digits(sum_numbers(stringf)))