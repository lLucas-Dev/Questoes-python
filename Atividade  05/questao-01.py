array1 = [1,2,3,4,5,3,2,6,1,5]
array2 = []


for i in range (len(array1)):
    for j in range (i + 1, (len(array1))):
        if(array1[i] == array1[j]):
            array2.append(array1[i])


print(array2)