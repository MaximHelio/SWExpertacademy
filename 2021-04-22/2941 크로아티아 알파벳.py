word = input()
alpha = ['c=', 'c-', 'dz=', 'd-','lj', 'nj', 's=', 'z=' ]

for letter in alpha:
    word = word.replace(letter, '1')
print(len(word))