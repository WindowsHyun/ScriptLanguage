s = input("영단어들 입력:")
t = []
for x in s:
    if x != ' ':
        t.append(x)

d = dict()

for x in t:
    if x in d.keys():
        d[x] +=1
    else:
        d[x] = 1

for k,v in d.items():
    print(k, "빈도수 : ", v)
