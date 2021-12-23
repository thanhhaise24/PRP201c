def check_ordered(s):
    flag = ''
    ck = sorted(s)
    for i in ck:
        flag += i
    return flag


data = open('words.txt')

res = []
words = []

for line in data:
    piece = line.split()
    for i in piece:
        if ',' in piece or '.' in i:
            words.append(i[0:len(i)-1])
        words.append(i)

for i in words:
    if check_ordered(i) == i:
        res.append(i)

print('The ordered words:')
print(res)