file = open('file.txt', 'r')
print(file.read())
file.close()

file = open('file.txt', 'r')
print("\n Read in parts \n")
print(file.read(9))
file.close()

file = open('filel.txt', 'a')
file.write(' Hi! I am Penguin and I am 35 yr old.')
file.close()