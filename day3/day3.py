def openfile():
    file = open("day3/day3input.txt", "r")
    return file


def count_bits(file):
    bits_array = []
    for binary in [line.strip() for line in file.readlines()]:
        for i in range(len(binary)):
            if len(bits_array) < i + 1:
                bits_array.append(0)
            if binary[i] == "1":
                bits_array[i] += 1
            else:
                bits_array[i] -= 1
    return bits_array


def gamma(bits_array):
    gamma_array = ["1" if x > 0 else "0" for x in bits_array]
    return int("".join(gamma_array), 2)


def epsilon(bits_array):
    epsilon_array = ["1" if x <= 0 else "0" for x in bits_array]
    return int("".join(epsilon_array), 2)


def main():
    file = openfile()
    bits_array = count_bits(file)
    result = gamma(bits_array) * epsilon(bits_array)
    print(str(result))


if __name__ == "__main__":
    main()
