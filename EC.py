from sys import argv
text = argv[1]
line_1 = []
line_2 = []
line_3 = []
for number, char in enumerate(text):
    if number % 4 == 0:
        line_1.append(char)
    elif number % 2 != 0:
        line_2.append(char)
    elif number % 2 == 0:
        line_3.append(char)
print(''.join(line_1)+''.join(line_2)+''.join(line_3))
