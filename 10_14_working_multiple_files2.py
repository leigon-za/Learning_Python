def count_words(filenames):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['lazarus.txt','nietsczhe.txt','plato_the_republic.txt','pride_prejudic.txt']
for filename in filenames:
    count_words(filenames)