import sys 

def symbolOne(arr, count):
    for x in range(count):
        num = (int)(float(arr[x][1]))
        if (num > 265 and num < 325):
            arr[x][3] = 'm'
        elif (num > 153 and num < 213):
            arr[x][3] = 't'
        elif (num > 32 and num < 92):
            arr[x][3] = 'p'
        else:
            arr[x][3] = 'ERROR '
    return arr

def symbolTwo(arr, count):
    for x in range(count):
        num = (int)(float(arr[x][2]))
        if (num > 120 and num < 205):
            arr[x][3] = arr[x][3] + 't'
        elif (num > 35 and num < 105):
            arr[x][3] = arr[x][3] + 'p'
        else:
            arr[x][3] = arr[x][3] + ' ERROR' 
    return arr


def main(argv): 
    with open(r'__FILE_PATH__') as f:
        arrLines = f.readlines()
    with open(r'__FILE_PATH__') as fp:
        for count, line in enumerate(fp):
            pass
    count = (int)((count + 1)/3)
    pVal = [[0]*3 for i in range(count)]
    rVal = [[0]*3 for i in range(count)]
    for x in range(count):
        pVal[x] = arrLines[x*3 + 1].split("    ")
        pVal[x][2] = pVal[x][2].strip()
        pVal[x][3] = pVal[x][3].strip()
        rVal[x] = arrLines[x*3 + 2].split("    ")
        rVal[x][2] = rVal[x][2].strip()
        rVal[x][3] = rVal[x][3].strip()
    pVal = symbolOne(pVal, count)
    pVal = symbolTwo(pVal, count)
    rVal = symbolOne(rVal, count)
    rVal = symbolTwo(rVal, count)

    for x in range(count):
        print(arrLines[x*3] + 'P: ' + pVal[x][3] +  ' R: ' + rVal[x][3])
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
