def mySort(sort_list):
    length = len(sort_list)
    i = 0
    for i in range(length-1):
        counter = 0
        for counter in range(length-1):
            if (sort_list[counter] > sort_list[counter+1]):
                temp = sort_list[counter]
                sort_list[counter] = sort_list[counter+1]
                sort_list[counter+1] = temp
                counter += 1
            else:
                counter +=1
        i += 1
    print("Sorted list: {}".format(sort_list))
        

sort_lista = [67, 45, 2, 13, 1, 998]
print("Presorted list: {}".format(sort_lista))
mySort(sort_lista)

sort_listb = [89, 23, 33, 45, 10, 12, 45, 45, 45]
print("Presorted list: {}".format(sort_listb))
mySort(sort_listb)
