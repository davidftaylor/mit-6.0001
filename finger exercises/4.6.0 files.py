##nameHandle = open('kids', 'w')
##for i in range(2):
##    name = input('Enter name: ')
##    nameHandle.write(name + '\n')
##nameHandle.close()
##
##nameHandle = open('kids', 'r')
##for line in nameHandle:
##    print(line)
##nameHandle.close()

nameHandle = open('kids', 'w')
nameHandle.write('David\n')
nameHandle.write('Bryn\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()

nameHandle = open('kids', 'a')
nameHandle.write('Tobo\n')
nameHandle.write('Dingo\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()
