fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if len(word) > 9:
        count += 1
        print(word)
print("The count was:", count)
