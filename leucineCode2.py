import sys 

def symbolOne(arr, count):
    for x in range(count):
        num1 = (int)(float(arr[x][1]))
        num2 = (int)(float(arr[x][2]))
        #p
        if (num1 > 32 and num1 < 92):
            if (num2 > 50 and num2 < 110):
                arr[x][3] = 'pp'
        #t
        if (num1 > 153 and num1 < 213):
            if (num2 > 35 and num2 < 95):
                arr[x][3] = 'tp'
        if (num1 > 158 and num1 < 218):
            if (num2 > 115 and num2 < 175):
                arr[x][3] = 'tt'
        #m
        if (num1 > 245 and num1 < 305):
            if (num2 > 35 and num2 < 95):
                arr[x][3] = 'mp'
        if (num1 > 265 and num1 < 325):
            if (num2 > 145 and num2 < 205):
                arr[x][3] = 'mt'
    return arr

def main(argv): 
    with open(r'C:\Users\vjoji\Desktop\Chechi\rotamers.dat') as f:
        arrLines = f.readlines()
    with open(r'C:\Users\vjoji\Desktop\Chechi\rotamers.dat') as fp:
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
    rVal = symbolOne(rVal, count)

    for x in range(count):
        print(arrLines[x*3] + 'P: ' + pVal[x][3] +  ' R: ' + rVal[x][3])
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
