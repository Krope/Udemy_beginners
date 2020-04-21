with open('file_1.txt') as file:
    line_number = 1
    for line in file:
        print('{}: {}'.format(line_number, line.rstrip()))
        line_number += 1
