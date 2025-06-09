file_read = open('file.txt','r')
print("File in read mode -")
print(file_read.read())
file_read.close()

file_write = open( 'file.txt', 'w')

file_write.write('File in write mode ....')
file_write.write('Hi!, I am penguin, I am 1 years old')
file_write.close()

file_append = open('file.txt', 'a')

file_append.write("\n File in append mode ....")
file_append.write('Hi!, I am penguin, I am 1 years old')
file_append.close()