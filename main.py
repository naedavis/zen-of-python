#finding the longest word in the sen of python
with open('zen-of-python.txt', 'r') as zen:
    words = []
    for line in zen:
        x = line.split()
        words = words + x
        words.sort()
    print( "Longest word : " + words[-1])
#counting the number of lines in zen of python
with open('zen-of-python.txt') as lines:
    counter = 0
    for line in lines:
        counter = counter + 1
    print( "there are " + str(counter) + "lines in this textfile")
