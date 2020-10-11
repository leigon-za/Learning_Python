filename = 'alice.txt'

with open(filename, encoding = 'utf-8') as f:
    contents= f.read

#This must produce an error because the txt file is not yet created