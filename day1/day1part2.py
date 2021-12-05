import os

def openfile():
    file = open(os.path.join(os.path.dirname(__file__), 'day1input.txt'), 'r')
    return file

def closefile(file):
    file.close()

def sliding_window(file):
    count = 0
    line_cpt = 0
    cpt = 9999 # to avoid first line to be counted

    lines = file.readlines()

    for line in lines:
        line_cpt += 1
        if(line_cpt < len(lines) - 1):
            sum1 = int(line.strip()) + int(lines[line_cpt].strip()) + int(lines[line_cpt+1].strip())
            #sum2 = int(line[line_cpt].strip()) + int(lines[line_cpt+1].strip()) + int(lines[line_cpt+2].strip())
            print(cpt, sum1)
            if(sum1 > cpt):
                count += 1
            cpt = sum1
    return count

def __main__():
    file = openfile()
    print(sliding_window(file))
    closefile(file)

if __name__ == "__main__":
    __main__()