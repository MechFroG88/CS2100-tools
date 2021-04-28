import string

alpha = list(string.ascii_uppercase)

def minimum():
    # input bits of opcodes
    # eg : 6 10 25 30 32
    arr = list(map(int,input("Bits of opcodes : ").split()))
    arr.sort()
    ans = (1 << arr[-1]) + (len(arr)-1)
    for i in range(len(arr)-1):
        ans -= 1 << (arr[-1] - arr[i])
    print(ans)

def maximum():
    # input bits of opcodes
    # eg : 6 10 25 30 32"
    arr = list(map(int,input("Bits of opcodes : ").split()))
    arr.sort()
    ans = 1
    arr = [0] + arr
    for i in range(1, len(arr)):
        ans += (1 << (arr[i] - arr[i-1])) - 1
    print(ans)

def printKmap(matrix, n, var):
    print("-"*30)
    print("Kmap for " + matrix[0][n])
    # n = 2
    if (len(var) == 2) :
        arr = ["", f"{var[1]}'", f"{var[1]}"]
        print("\t|".join(arr))
        arr = [f"{var[0]}'", matrix[1][n], matrix[2][n]]
        print("\t|".join(arr))
        arr = [f"{var[0]}", matrix[3][n], matrix[4][n]]
        print("\t|".join(arr))
    
    # n = 3
    if (len(var) == 3) :
        arr = ["", f"{var[1]}'.{var[2]}'", f"{var[1]}'.{var[2]}", f"{var[1]}.{var[2]}", f"{var[1]}.{var[2]}'"]
        print("\t|".join(arr))
        arr = [f"{var[0]}'", matrix[1][n], matrix[2][n], matrix[4][n], matrix[3][n]]
        print("\t|".join(arr))
        arr = [f"{var[0]}", matrix[5][n], matrix[6][n], matrix[8][n], matrix[7][n]]
        print("\t|".join(arr))
    
    # n = 4
    if (len(var) == 4) :
        arr = ["", f"{var[2]}'.{var[3]}'", f"{var[2]}'.{var[3]}", f"{var[2]}.{var[3]}", f"{var[2]}.{var[3]}'"]
        print("\t|".join(arr))
        arr = [f"{var[0]}'.{var[1]}'", matrix[1][n], matrix[2][n], matrix[4][n], matrix[3][n]]
        print("\t|".join(arr))
        arr = [f"{var[0]}'.{var[1]}", matrix[5][n], matrix[6][n], matrix[8][n], matrix[7][n]]
        print("\t|".join(arr))
        arr = [f"{var[0]}.{var[1]}",matrix[13][n], matrix[14][n], matrix[16][n], matrix[15][n]]
        print("\t|".join(arr))
        arr = [f"{var[0]}.{var[1]}'", matrix[9][n], matrix[10][n], matrix[12][n], matrix[11][n]]
        print("\t|".join(arr))

def minterm():
    # input number of bits
    # eg : 4
    n = int(input("Bits of state : "))

    # input minterms
    # eg : 5 3 2 1
    m = list(map(int,input("Minterms : ").split()))

    # input dontcares
    # eg : 0 4 6 8
    x = list(map(int,input("Dont cares : ").split()))

    matrix = []
    firstRow = [""] + alpha[:n]
    firstRow.append('Output')
    matrix.append(firstRow)
    for i in range(1 << n):
        row = [str(i)] + list(bin(i)[2:].zfill(n))
        if (i in m) :
            row.append('1')
        elif (i in x) :
            row.append('x')
        else :
            row.append('0')
        matrix.append(row)

    printMatrix(matrix, 1)
    printKmap(matrix, n, alpha[:n])

def maxterm():
    # input number of bits
    # eg : 4
    n = int(input("Bits of state : "))

    # input minterms
    # eg : 5 3 2 1
    m = list(map(int,input("Maxterms : ").split()))

    # input dontcares
    # eg : 0 4 6 8
    x = list(map(int,input("Dont cares : ").split()))

    matrix = []
    firstRow = [""] + alpha[:n]
    firstRow.append('Output')
    matrix.append(firstRow)
    for i in range(1 << n):
        row = [str(i)] + list(bin(i)[2:].zfill(n))
        if (i in m) :
            row.append('0')
        elif (i in x) :
            row.append('x')
        else :
            row.append('1')
        matrix.append(row)

    printMatrix(matrix, 1)
    printKmap(matrix, n, alpha[:n])

def flip():
    # input number of bits
    # eg : 4
    n = int(input("Bits of state : "))

    # input bits of input
    # eg : 2
    inputs = int(input("Bits of input : "))
    inputAlpha = []

    if (inputs != 0):
        inputAlpha = list(input("Alphabet for input(s) : "))

    # input flip-flop type
    # eg : D T JK SR
    types = input("Flip-flop type of state : ").upper().split()

    arr = []

    var = alpha[:n] + inputAlpha

    for j in range(n):
        flipflop = types[j]
        arr += [input(f"input for {i}{var[j]} : ").upper().replace(" ","") for i in flipflop]
    
    matrix = []
    
    firstRow = var + list(map(lambda x : x + "+", alpha[:n]))

    for i in range(n):
        flipflop = types[i]
        firstRow += list(map(lambda x : x + alpha[i], flipflop))
    firstRow = [""] + firstRow
    matrix.append(firstRow)

    for i in range(1 << (n + inputs)):
        row = [str(i)] + list(bin(i)[2:].zfill(n + inputs))
        newArr = arr.copy()
        for j in range(n + inputs):
            if (i & (1 << (n + inputs - j - 1))):
                newArr = list(map(lambda x : x.replace(f"{var[j]}'", "0"), newArr))
                newArr = list(map(lambda x : x.replace(f"{var[j]}", "1"), newArr))
            else:
                newArr = list(map(lambda x : x.replace(f"{var[j]}'", "1"), newArr))
                newArr = list(map(lambda x : x.replace(f"{var[j]}", "0"), newArr))
        result = [j.count('0') == 0 and j.count('1') != 0 for j in newArr]
        index = 0
        valid = True
        for j in range(n):
            flipflop = types[j]
            if (flipflop == 'D'):
                row.append(str(result[index]))
                index += 1
            if (flipflop == 'T'):
                if (result[index]):
                    row.append("1" if row[j+1] == "0" else "0")
                else:
                    row.append(row[j+1])
                index += 1
            if (flipflop == 'JK'):
                if (result[index] and result[index+1]):
                    row.append("1" if row[j+1] == "0" else "0")
                if (result[index] and not result[index+1]):
                    row.append("1")
                if (not result[index] and result[index+1]):
                    row.append("0")
                if (not result[index] and not result[index+1]):
                    row.append(row[j+1])
                index += 2
            if (flipflop == 'SR'):
                if (result[index] and result[index+1]):
                    valid = False
                if (result[index] and not result[index+1]):
                    row.append("1")
                if (not result[index] and result[index+1]):
                    row.append("0")
                if (not result[index] and not result[index+1]):
                    row.append(row[j+1])
                index += 2
        if (valid):
            matrix.append(row + result)
    
    printMatrix(matrix, 1)

    print("-"*30)
    for row in matrix[1:]:
        if (inputs == 0):
            print(f'{int("".join(row[1:n+1]), 2)} ---> {int("".join(row[n+1:2*n+1]), 2)}')
        else :
            print(f'{int("".join(row[1:n+1]), 2)} --{int("".join(row[n+1:n+1+inputs]), 2)}--> {int("".join(row[n+1+inputs:n+1+inputs+n]), 2)}')
    print("-"*30)

def state():
    # input number of bits
    # eg : 4
    n = int(input("Bits of state : "))

    # input bits of inputs
    # eg : 2
    inputs = int(input("Bits of inputs : "))

    # input flip-flop type
    # eg : D T JK SR
    types = input("Flip-flop type of state : ").upper().split()

    # input number of edges
    # eg : 5
    m = int(input("Number of edges : "))

    graph = [-1 for i in range(1 << (n + inputs))]

    # input edges
    # from_node to_node input
    # eg : 1 3 1
    for i in range(m):
        temp = input(f"Edge {i+1} : ").split()
        fromNode = int(temp[0])
        toNode = int(temp[1])
        if (inputs != 0):
            fromNode = (fromNode << inputs) + int(temp[2])
        graph[fromNode] = toNode
    matrix = []

    # A B C Y Z A+ B+ C+
    var = alpha[:n] + alpha[26-(inputs):]
    firstRow = list(map(lambda x : x + "+", alpha[:n]))

    # JA KA DB DC
    for i in range(n):
        flipflop = types[i]
        firstRow += list(map(lambda x : x + alpha[i], flipflop))
    firstRow = [""] + firstRow
    matrix.append(firstRow)

    activation = {
        "D" : [["0"], ["1"], ["0"], ["1"]],
        "T" : [["0"], ["1"], ["1"], ["0"]],
        "JK" : [["0","x"], ["1","x"], ["x","1"], ["x","0"]],
        "SR" : [["0","x"], ["1","0"], ["0","1"], ["x","0"]],
        }

    for i in range(1 << (n + inputs)):
        row = [str(i)] + list(bin(i)[2:].zfill(n + inputs))

        toNode = graph[i]
        fromNode = i >> inputs

        # no next state
        if (toNode == -1) :
            row += ["x" for i in range(len(firstRow) - n - 1 - inputs)]
            matrix.append(row)
            continue

        v = bin(toNode)[2:].zfill(n)
        row += list(v)
            
        # for each flipflop
        for j in range(n):
            index = 2 * ((fromNode >> (n-j-1)) & 1) + (toNode >> (n-j-1) & 1)
            row += activation[types[j]][index]
        matrix.append(row)

    printMatrix(matrix, 1)
    
    for i in range(n * 2 + inputs + 1, len(firstRow)):
        printKmap(matrix, i, var)

def cache():
    # input cache type
    # eg : 4
    cacheType = int(input("Select Cache Type (Input the row number): \
    \n 1. Least Recently Used (LRU)\
    \n 2. First in First out (FIFO)\
    \n 3. Least Frequently Used (LFU) \n"))

    if cacheType not in [1,2,3]:
        return

    # input number of words
    # eg : 4
    words = int(input("Number of words in a cache block : "))

    # input number of words
    # eg : 4
    memory = int(input("Total number of words in cache memory : "))

    # input number of blocks
    # eg : 2
    sets = int(input("Number of block in a set : "))

    import math 
    print("-"*30)
    cacheOffset = int(math.log2(words)) + 2
    print("Offset : " + str(cacheOffset))

    setIndex = int(math.log2(memory/(words*sets)))
    print("Set/block index : " + str(setIndex))
    print("-"*30)

    # input number of arrays
    # eg : 2
    arr = []

    cacheMem = [[[0,0,[]] for j in range(sets)] for i in range (1 << setIndex)]

    for i in range(int(input("Number of array in memory : "))) :
        arr.append(int(input("Address of array " + chr(ord('A') + i) + " : "), 16))

    print("-"*30)
    def convertHex(i):
        return "0x" + hex(i)[2:].zfill(8)

    hits = [0 for i in range(len(arr))]
    miss = [0 for i in range(len(arr))]
    time = 0

    while True:
        time += 1
        inp = input("Memory access : ").upper()
        if (inp == 'Q') :
            break
        if (inp == 'C') :
            cacheMem = [[[0,0,[]] for j in range(sets)] for i in range (1 << setIndex)]
            hits = [0 for i in range(len(arr))]
            miss = [0 for i in range(len(arr))]
            time = 0
            print('Cache cleared!')
            continue
        newinp = []
        for mem in inp.split():
            if ('-' in mem):
                start = int(mem.split('[')[1].split('-')[0])
                end = int(mem.split('[')[1].split('-')[1][:-1])
                for i in range(start, end+1):
                    newinp.append(f'{mem.split("[")[0]}[{i}]')
            else :
                newinp.append(mem)
        for mem in newinp:
            array = ord(mem.split('[')[0]) - ord('A')
            index = int(mem.split('[')[1][:-1])
            mem = arr[array] + index * 4
            tag = mem >> (cacheOffset + setIndex)
            index = (mem >> cacheOffset) & ((1 << setIndex) - 1)
            offset = mem & ((1 << cacheOffset) - 1)
            print("-"*30)
            print(f'Accessing {mem}, {convertHex(mem)}')
            print(f'Tag : {tag}, {convertHex(tag)}')
            print(f'Index : {index}, {convertHex(index)}')
            print(f'Offset : {offset}, {convertHex(offset)}')
            print(f'Time : {time}')
            hit = False
            for i in cacheMem[index]:
                if (mem in i[2]):
                    hit = True
                    if (cacheType == 1):
                        i[0] = time
                    elif (cacheType == 3):
                        i[0] += 1
                    break

            if (not hit):
                miss[array] += 1
                minimum = time
                replace = 0
                for i in range(sets):
                    if (cacheMem[index][i][0] < minimum):
                        minimum = cacheMem[index][i][0]
                        replace = i
                cacheMem[index][replace][0] = 1 if cacheType == 3 else time
                cacheMem[index][replace][1] = array
                cacheMem[index][replace][2] = [((mem >> cacheOffset) << cacheOffset) + i*4 for i in range(words)]
            else :
                hits[array] += 1

            if hit:
                print("HIT!!!")
            else:
                print("It is a miss...")
            print()

        matrix = []
        firstRow = [f'Block {i}' for i in range(sets)]
        firstRow = [''] + firstRow
        matrix.append(firstRow)
        for i in range(len(cacheMem)) :
            row = [str(i)]
            for j in range(len(cacheMem[i])) :
                temp = []
                for k in range(len(cacheMem[i][j][2])):
                    temp.append(f'{chr(ord("A") + cacheMem[i][j][1])}[{(cacheMem[i][j][2][k] - arr[cacheMem[i][j][1]])//4}]')
                row.append(",".join(temp))
            matrix.append(row)

        printMatrix(matrix, 5)

        for i in range(len(hits)):
            print(f'Hit rate for array {chr(ord("A") + i)} : {hits[i]}/{hits[i] + miss[i]}')
        print("-"*30)
        print("input 'C' to clear cache \ninput 'Q' to quit")

def printMatrix(matrix, space):
    mx = max((len(str(ele)) for sub in matrix for ele in sub))
    for row in matrix:
        print("||".join(["{:<{mx}}".format(ele,mx=mx + space) for ele in row]))


while True:
    print("Welcome to CS2100 tools. Input the row number of the tool you wish to use")
    option = int(input("Options : \
    \n 1. Find maximum opcodes \
    \n 2. Find minimum opcodes \
    \n 3. Generate Truth table and k-map given min-terms \
    \n 4. Generate Truth table and k-map given max-terms \
    \n 5. Generate state diagram given flip-flop inputs \
    \n 6. Generate Truth table and k-map given state diagram \
    \n 7. Cache Visualizer\n"))
    if option not in [i+1 for i in range(7)]:
        break
    
    if (option == 1) :
        minimum()
    if (option == 2) :
        maximum()
    if (option == 3) :
        minterm()
    if (option == 4) :
        maxterm()
    if (option == 5) :
        flip()
    if (option == 6) :
        state()
    if (option == 7) :
        cache()
    print()
    input("Press ENTER to continue")


