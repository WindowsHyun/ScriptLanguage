s = input("10개 숫자 입력 : ")
list = s.split()
list2 = []
numbers = [int(x) for x in list]

counts = [0]*100

for x in numbers:
    counts[x-1] += 1

for x in range(100):
    if counts[x] > 0:
        list2 += [x+1]

print(list2)
