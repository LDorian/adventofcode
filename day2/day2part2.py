import os


def openfile():
    file = open(os.path.join(os.path.dirname(__file__), "day2input.txt"), "r")
    return file


def submarine_move(file):
    x = 0
    y = 0
    aim = 0
    for line in file:
        line = line.strip()
        if line[0] == "f":
            x += int(line[-1])
            y += aim * int(line[-1])
        elif line[0] == "u":
            aim -= int(line[-1])
        elif line[0] == "d":
            aim += int(line[-1])
    return x * y


def main():
    file = openfile()
    print(submarine_move(file))


if __name__ == "__main__":
    main()
