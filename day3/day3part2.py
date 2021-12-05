def openfile():
    file = open("day3/day3input.txt", "r")
    return file


def counter(file):
    bits_array = [line.strip() for line in file.readlines()]
    o2 = [[char for char in line] for line in bits_array]
    return bits_array, o2


def o2_rating(bits_array, o2):
    for i in range(len(bits_array[0])):
        if len(o2) > 1:
            o2 = [
                x
                for x in o2
                if x[i]
                == (
                    "1"  # If the number of 1s is greater than the number of 0s, the row is 1, otherwise it is 0
                    if (
                        len(
                            [x for x in o2 if x[i] == "1"]
                        )  # Counts the number of 1s in the row
                        >= len(
                            [x for x in o2 if x[i] == "0"]
                        )  # Counts the number of 0s in the row
                    )
                    else "0"
                )
            ]
    return int("".join(o2[0]), 2)


def co2_rating(bits_array, o2):
    for i in range(len(bits_array[0])):
        if len(o2) > 1:
            o2 = [
                x
                for x in o2
                if x[i]
                == (
                    "0"  # If the number of 1s is greater than the number of 0s, the row is 1, otherwise it is 0
                    if (
                        len(
                            [x for x in o2 if x[i] == "1"]
                        )  # Counts the number of 1s in the row
                        >= len(
                            [x for x in o2 if x[i] == "0"]
                        )  # Counts the number of 0s in the row
                    )
                    else "1"
                )
            ]
    return int("".join(o2[0]), 2)


def main():
    file = openfile()
    bits_array, o2 = counter(file)
    result = o2_rating(bits_array, o2) * co2_rating(bits_array, o2)
    print(str(result))


if __name__ == "__main__":
    main()
