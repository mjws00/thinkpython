fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if len(word) > 13:
        count += 1
        print(word)
print("The count was:", count)
