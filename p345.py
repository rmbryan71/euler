result = []
inputfile = open('p345_example.txt', 'r')
for line in inputfile.readlines():
    result.append([int(x) for x in line.split(',')])



