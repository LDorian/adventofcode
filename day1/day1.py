import os

def openfile():
    file = open(os.path.join(os.path.dirname(__file__), 'day1input.txt'), 'r')
    return file

def count_increase(file):
    count = 0
    cpt = 9999 # to avoid first line to be counted
    for line in file:
        if cpt < int(line):
            count += 1
        cpt = int(line)
    return count

def __main__():
    file = openfile()
    print(count_increase(file))

if __name__ == "__main__":
    __main__()