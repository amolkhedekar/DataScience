items = input().split(',')
result = []
for i in items:
    value = int(i, 2)
    if value % 5 == 0:
        result.append(i)

for item in result:
    print(item, end=",")
