words = list(input().split(' '))
unique_words = set(words)
sorted_list = sorted(unique_words)
for i in sorted_list:
    print(i, end=' ')
