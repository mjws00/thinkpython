count_total = 0
count_no_e = 0

fin = open("words.txt")

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

for word in fin:
    if has_no_e(word) == True:
        print(word.strip())
        count_no_e += 1
    count_total += 1

print()
print('There are', count_no_e, 'words with no e.')
print("That is:", count_no_e/count_total * 100, "percent.")