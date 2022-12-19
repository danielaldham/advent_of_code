txtfile = 'day1_input.txt'

count = []
cals = 0

file = open(txtfile, 'r')

for line in file:
    if line == '\n':
        count.append(cals)
        cals = 0
    else:
        cals += int(line)

print(max(count))