def merge(list1, list2):
    num = len(list1) +len(list2)
    list3 = [0]*num

    for x in range(len(list1)):
        print(x)
        list3[x] += list1[x]

    for x in range(len(list1), len(list1)+len(list2), +1):
        print(x)
        list3[x] += list2[x-len(list1)]

    for i in range(len(list1)+len(list2)):
        for j in range(len(list1)+len(list2)-1):
            if (list3[j] > list3[j+1]):
                list3[j], list3[j+1] = list3[j+1], list3[j]
            
        

    print(list3)
    
