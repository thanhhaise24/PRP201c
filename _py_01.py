# Enter an integer
while(True):
        try:
            num = int(input('Enter a positive number: '))
            if num <= 0:
                raise Exception
            break
        except:
            print('The number must be a positive')

hex = ''
re = []
n = num

# Convert
while n != 0:
    r = n % 16
    n = int(n/16)
    re.append(r)

for i in reversed(re):
    if i == 10:
        hex += 'A'
    elif i == 11:
        hex += 'B'
    elif i == 12:
        hex += 'C'
    elif i == 13:
        hex += 'D'
    elif i == 14:
        hex += 'E'
    elif i == 15:
        hex += 'F'
    else:
        hex += str(i)

print(f'{num} is converted into hexadecimal: {hex}')
    