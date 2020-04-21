with open('file_2.txt') as file:
    word_sort = list(file)
    ws = sorted(word_sort)
    for word in ws:
        print(word)
