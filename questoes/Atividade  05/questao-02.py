array = ['PYTHON', 'java', 'JAVASCRIPT', 'C', 'RUBY']
array2 = []
for i in range(len(array)):
    if (len(array[i]) > 4 and array[i].isupper()):
        array2.append(array[i])

print(array2)


