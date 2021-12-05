import os

def openfile():
    file = open(os.path.join(os.path.dirname(__file__), 'day2input.txt'), 'r')
    return file

def submarine_move(file):
    x = 0
    y = 0
    for line in file:
        line = line.strip()
        if line[0] == 'f':
            x += int(line[-1])
        elif line[0] == 'u':
            y += int(line[-1])
        elif line[0] == 'd':
            y -= int(line[-1])
    return x, y

def main():
    file = openfile()
    x, y = submarine_move(file)
    print(abs(x * y))

if __name__ == '__main__':
    main()
