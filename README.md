# CS2100-tools
A set of tools dedicated for CS2100 of National University of Singapore (NUS).

Feel free to contact me if you found any bugs or have ideas for improvement.

# Installation

Works on any version of python 3

```bash
python cs2100.py
```

# Tools

1. Find maximum opcodes 
2. Find minimum opcodes 
3. Generate Truth table and k-map given min-terms 
4. Generate Truth table and k-map given max-terms
5. Generate state diagram given flip-flop inputs
6. Generate Truth table and k-map given state diagram
7. Cache Visualizer


# Find Maximum Opcodes
Find maximum number of instructions available using expanding opcode scheme given number of bits of opcodes of different classes of instruction

## Input format

Number of bits of opcodes of different classes of instruction seperated by space

### Example Input
```
Bits of opcodes : 4 6 8
```
### Example Output
```
238
```

# Find Minimum Opcodes
Find minimum number of instructions available using expanding opcode scheme given number of bits of opcodes of different classes of instruction

## Input format

Number of bits of opcodes of different classes of instruction seperated by space

### Example Input
```
Bits of opcodes : 4 6 8
```
### Example Output
```
22
```

# Generate Truth table and k-map given min-terms 
Generate Truth table and k-map given min-terms and dontcares (optional)


## Input format

First line input number of bits

Second line input min-terms seperated by space

Third line input dontcares seperated by space (leave empty if there are no dontcares)

### Example Input
```
Bits of state : 4
Minterms : 1 2 3 4
Dont cares : 5 6 7 8
```
### Example Output
```
       ||A      ||B      ||C      ||D      ||Output
0      ||0      ||0      ||0      ||0      ||0
1      ||0      ||0      ||0      ||1      ||1
2      ||0      ||0      ||1      ||0      ||1
3      ||0      ||0      ||1      ||1      ||1
4      ||0      ||1      ||0      ||0      ||1
5      ||0      ||1      ||0      ||1      ||x
6      ||0      ||1      ||1      ||0      ||x
7      ||0      ||1      ||1      ||1      ||x
8      ||1      ||0      ||0      ||0      ||x
9      ||1      ||0      ||0      ||1      ||0
10     ||1      ||0      ||1      ||0      ||0
11     ||1      ||0      ||1      ||1      ||0
12     ||1      ||1      ||0      ||0      ||0
13     ||1      ||1      ||0      ||1      ||0
14     ||1      ||1      ||1      ||0      ||0
15     ||1      ||1      ||1      ||1      ||0
------------------------------
Kmap for Output
        |C'.D'  |C'.D   |C.D    |C.D'
A'.B'   |0      |1      |1      |1
A'.B    |1      |x      |x      |x
A.B     |0      |0      |0      |0
A.B'    |x      |0      |0      |0
```

# Generate Truth table and k-map given max-terms 
Generate Truth table and k-map given max-terms and dontcares (optional)


## Input format

First line input number of bits

Second line input max-terms seperated by space

Third line input dontcares seperated by space (leave empty if there are no dontcares)

### Example Input
```
Bits of state : 4
Minterms : 1 2 3 4
Dont cares : 5 6 7 8
```
### Example Output
```
       ||A      ||B      ||C      ||D      ||Output
0      ||0      ||0      ||0      ||0      ||1
1      ||0      ||0      ||0      ||1      ||0
2      ||0      ||0      ||1      ||0      ||0
3      ||0      ||0      ||1      ||1      ||0
4      ||0      ||1      ||0      ||0      ||0
5      ||0      ||1      ||0      ||1      ||x
6      ||0      ||1      ||1      ||0      ||x
7      ||0      ||1      ||1      ||1      ||x
8      ||1      ||0      ||0      ||0      ||x
9      ||1      ||0      ||0      ||1      ||1
10     ||1      ||0      ||1      ||0      ||1
11     ||1      ||0      ||1      ||1      ||1
12     ||1      ||1      ||0      ||0      ||1
13     ||1      ||1      ||0      ||1      ||1
14     ||1      ||1      ||1      ||0      ||1
15     ||1      ||1      ||1      ||1      ||1
------------------------------
Kmap for Output
        |C'.D'  |C'.D   |C.D    |C.D'
A'.B'   |1      |0      |0      |0
A'.B    |0      |x      |x      |x
A.B     |1      |1      |1      |1
A.B'    |x      |1      |1      |1
```

# Generate state diagram given flip-flop inputs
Generate state diagram given flip-flop inputs

## Input format

1. Input number of flip-flops

2. Input bits of input (0 if none)

3. If there's input, the next line should input variable for input. Any variable works fine as long as it doesn't crash with state variable.

Examples for 1 bit input
```
Variable for input : X
```
```
Variable for input : Y
```

Examples for 2 bit input
```
Variable for input : XY
```
```
Variable for input : YZ
```
```
Variable for input : HY
```

4. Input flip-flop types seperated by space. The type of flip-flop must be either "D" or "T" or "JK" or "SR". You should input n types of flip-flop if you have n flip-flops

5. Input the inputs for flipflop. The program currently only support Sum of Products (SOP) inputs.

The following input are equivalent
```
A'B + CX' 
Ba' + X'c 
A'.B + C.x'
a'b+CX'
a' b  +  c x'
```

### Example input 1

```
Bits of state : 3
Bits of input : 1
Variable for input : x
Flip-flop type of state : D T JK
input for DA : A'B + CX'
input for TB : ACX + BCX
input for JC : AX' + BC
input for KC : AB' + XC
```

### Example output 1

```
      ||A     ||B     ||C     ||x     ||A+    ||B+    ||C+    ||DA    ||TB    ||JC    ||KC
0     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||0
1     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||0
2     ||0     ||0     ||1     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||0
3     ||0     ||0     ||1     ||1     ||0     ||0     ||1     ||0     ||0     ||0     ||0
4     ||0     ||1     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||0     ||0
5     ||0     ||1     ||0     ||1     ||0     ||1     ||0     ||0     ||0     ||0     ||0
6     ||0     ||1     ||1     ||0     ||1     ||1     ||1     ||1     ||0     ||0     ||0
7     ||0     ||1     ||1     ||1     ||1     ||1     ||1     ||1     ||0     ||0     ||0
8     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||0
9     ||1     ||0     ||0     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||0
10    ||1     ||0     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||1
11    ||1     ||0     ||1     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||1
12    ||1     ||1     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||0     ||0
13    ||1     ||1     ||0     ||1     ||0     ||1     ||0     ||0     ||0     ||0     ||0
14    ||1     ||1     ||1     ||0     ||0     ||0     ||1     ||0     ||1     ||1     ||0
15    ||1     ||1     ||1     ||1     ||0     ||0     ||1     ||0     ||1     ||1     ||0
------------------------------
0 --0--> 0
0 --1--> 0
1 --0--> 1
1 --1--> 1
2 --0--> 2
2 --1--> 2
3 --0--> 7
3 --1--> 7
4 --0--> 0
4 --1--> 0
5 --0--> 0
5 --1--> 0
6 --0--> 2
6 --1--> 2
7 --0--> 1
7 --1--> 1
------------------------------
```

### Example input 2

```
Bits of state : 4
Bits of input : 0
Flip-flop type of state : D T JK JK
input for DA : ABC + D
input for TB : D'C + B'A'
input for JC : A' + A'BC' + B'C'D'
input for KC : B'A + C
input for JD : C'
input for KD : ABCD' + A'B
```

### Example output 2
```
      ||A     ||B     ||C     ||D     ||A+    ||B+    ||C+    ||D+    ||DA    ||TB    ||JC    ||KC    ||JD    ||KD
0     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||0     ||1     ||0
1     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||0     ||1     ||0
2     ||0     ||0     ||1     ||0     ||0     ||1     ||1     ||0     ||0     ||1     ||0     ||0     ||0     ||0
3     ||0     ||0     ||1     ||1     ||0     ||0     ||1     ||1     ||0     ||0     ||0     ||0     ||0     ||0
4     ||0     ||1     ||0     ||0     ||0     ||1     ||0     ||1     ||0     ||0     ||0     ||0     ||1     ||0
5     ||0     ||1     ||0     ||1     ||0     ||1     ||0     ||1     ||0     ||0     ||0     ||0     ||1     ||0
6     ||0     ||1     ||1     ||0     ||0     ||1     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||0
7     ||0     ||1     ||1     ||1     ||0     ||1     ||1     ||1     ||0     ||0     ||0     ||0     ||0     ||0
8     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||0     ||1     ||0
9     ||1     ||0     ||0     ||1     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||0     ||1     ||0
10    ||1     ||0     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||0     ||1     ||0     ||0
11    ||1     ||0     ||1     ||1     ||0     ||0     ||0     ||1     ||0     ||0     ||0     ||1     ||0     ||0
12    ||1     ||1     ||0     ||0     ||0     ||1     ||0     ||1     ||0     ||0     ||0     ||0     ||1     ||0
13    ||1     ||1     ||0     ||1     ||0     ||1     ||0     ||1     ||0     ||0     ||0     ||0     ||1     ||0
14    ||1     ||1     ||1     ||0     ||0     ||1     ||1     ||0     ||0     ||0     ||0     ||0     ||0     ||0
15    ||1     ||1     ||1     ||1     ||1     ||1     ||1     ||1     ||1     ||0     ||0     ||0     ||0     ||0
------------------------------
0 ---> 1
1 ---> 1
2 ---> 6
3 ---> 3
4 ---> 5
5 ---> 5
6 ---> 6
7 ---> 7
8 ---> 1
9 ---> 1
10 ---> 0
11 ---> 1
12 ---> 5
13 ---> 5
14 ---> 6
15 ---> 15
------------------------------
```

# Generate Truth table and k-map given state diagram
Generate Truth table and k-map given state diagram
## Input format

1. Input number of flip-flops

2. Input bits of input (0 if none)

3. Input flip-flop types seperated by space. The type of flip-flop must be either "D" or "T" or "JK" or "SR". You should input n types of flip-flop if you have n flip-flops

4. Input number of edges (number of state transition)

5. Input edges in format `from_node to_node input`. Leave the input field empty if there's no input

### Example input 1
```
Bits of state : 4
Bits of inputs : 0
Flip-flop type of state : D T T JK
Number of edges : 11
Edge 1 : 1 3
Edge 2 : 3 5
Edge 3 : 5 7
Edge 4 : 7 9
Edge 5 : 9 11
Edge 6 : 11 13
Edge 7 : 13 15
Edge 8 : 15 2
Edge 9 : 2 4
Edge 10 : 4 6
Edge 11 : 6 1
```

### Example output 1
```
   ||A  ||B  ||C  ||D  ||A+ ||B+ ||C+ ||D+ ||DA ||TB ||TC ||JD ||KD
0  ||0  ||0  ||0  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x
1  ||0  ||0  ||0  ||1  ||0  ||0  ||1  ||1  ||0  ||0  ||1  ||x  ||0
2  ||0  ||0  ||1  ||0  ||0  ||1  ||0  ||0  ||0  ||1  ||1  ||0  ||x
3  ||0  ||0  ||1  ||1  ||0  ||1  ||0  ||1  ||0  ||1  ||1  ||x  ||0
4  ||0  ||1  ||0  ||0  ||0  ||1  ||1  ||0  ||0  ||0  ||1  ||0  ||x
5  ||0  ||1  ||0  ||1  ||0  ||1  ||1  ||1  ||0  ||0  ||1  ||x  ||0
6  ||0  ||1  ||1  ||0  ||0  ||0  ||0  ||1  ||0  ||1  ||1  ||1  ||x
7  ||0  ||1  ||1  ||1  ||1  ||0  ||0  ||1  ||1  ||1  ||1  ||x  ||0
8  ||1  ||0  ||0  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x
9  ||1  ||0  ||0  ||1  ||1  ||0  ||1  ||1  ||1  ||0  ||1  ||x  ||0
10 ||1  ||0  ||1  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x
11 ||1  ||0  ||1  ||1  ||1  ||1  ||0  ||1  ||1  ||1  ||1  ||x  ||0
12 ||1  ||1  ||0  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x
13 ||1  ||1  ||0  ||1  ||1  ||1  ||1  ||1  ||1  ||0  ||1  ||x  ||0
14 ||1  ||1  ||1  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x  ||x
15 ||1  ||1  ||1  ||1  ||0  ||0  ||1  ||0  ||0  ||1  ||0  ||x  ||1
------------------------------
Kmap for DA
        |C'.D'  |C'.D   |C.D    |C.D'
A'.B'   |x      |0      |0      |0
A'.B    |0      |0      |1      |0
A.B     |x      |1      |0      |x
A.B'    |x      |1      |1      |x
------------------------------
Kmap for TB
        |C'.D'  |C'.D   |C.D    |C.D'
A'.B'   |x      |0      |1      |1
A'.B    |0      |0      |1      |1
A.B     |x      |0      |1      |x
A.B'    |x      |0      |1      |x
------------------------------
Kmap for TC
        |C'.D'  |C'.D   |C.D    |C.D'
A'.B'   |x      |1      |1      |1
A'.B    |1      |1      |1      |1
A.B     |x      |1      |0      |x
A.B'    |x      |1      |1      |x
------------------------------
Kmap for JD
        |C'.D'  |C'.D   |C.D    |C.D'
A'.B'   |x      |x      |x      |0
A'.B    |0      |x      |x      |1
A.B     |x      |x      |x      |x
A.B'    |x      |x      |x      |x
------------------------------
Kmap for KD
        |C'.D'  |C'.D   |C.D    |C.D'
A'.B'   |x      |0      |0      |x
A'.B    |x      |0      |0      |x
A.B     |x      |0      |1      |x
A.B'    |x      |0      |0      |x
```

### Example input 2
```
Bits of state : 3
Bits of inputs : 1
Flip-flop type of state : D T JK
Number of edges : 5
Edge 1 : 1 2 0
Edge 2 : 2 3 0
Edge 3 : 3 4 0
Edge 4 : 4 5 1
Edge 5 : 5 6 1
```

### Example output 2
```
   ||A  ||B  ||C  ||Z  ||A+ ||B+ ||C+ ||DA ||TB ||JC ||KC
0  ||0  ||0  ||0  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x
1  ||0  ||0  ||0  ||1  ||x  ||x  ||x  ||x  ||x  ||x  ||x
2  ||0  ||0  ||1  ||0  ||0  ||1  ||0  ||0  ||1  ||x  ||1
3  ||0  ||0  ||1  ||1  ||x  ||x  ||x  ||x  ||x  ||x  ||x
4  ||0  ||1  ||0  ||0  ||0  ||1  ||1  ||0  ||0  ||1  ||x
5  ||0  ||1  ||0  ||1  ||x  ||x  ||x  ||x  ||x  ||x  ||x
6  ||0  ||1  ||1  ||0  ||1  ||0  ||0  ||1  ||1  ||x  ||1
7  ||0  ||1  ||1  ||1  ||x  ||x  ||x  ||x  ||x  ||x  ||x
8  ||1  ||0  ||0  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x
9  ||1  ||0  ||0  ||1  ||1  ||0  ||1  ||1  ||0  ||1  ||x
10 ||1  ||0  ||1  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x
11 ||1  ||0  ||1  ||1  ||1  ||1  ||0  ||1  ||1  ||x  ||1
12 ||1  ||1  ||0  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x
13 ||1  ||1  ||0  ||1  ||x  ||x  ||x  ||x  ||x  ||x  ||x
14 ||1  ||1  ||1  ||0  ||x  ||x  ||x  ||x  ||x  ||x  ||x
15 ||1  ||1  ||1  ||1  ||x  ||x  ||x  ||x  ||x  ||x  ||x
------------------------------
Kmap for DA
        |C'.Z'  |C'.Z   |C.Z    |C.Z'
A'.B'   |x      |x      |x      |0
A'.B    |0      |x      |x      |1
A.B     |x      |x      |x      |x
A.B'    |x      |1      |1      |x
------------------------------
Kmap for TB
        |C'.Z'  |C'.Z   |C.Z    |C.Z'
A'.B'   |x      |x      |x      |1
A'.B    |0      |x      |x      |1
A.B     |x      |x      |x      |x
A.B'    |x      |0      |1      |x
------------------------------
Kmap for JC
        |C'.Z'  |C'.Z   |C.Z    |C.Z'
A'.B'   |x      |x      |x      |x
A'.B    |1      |x      |x      |x
A.B     |x      |x      |x      |x
A.B'    |x      |1      |x      |x
------------------------------
Kmap for KC
        |C'.Z'  |C'.Z   |C.Z    |C.Z'
A'.B'   |x      |x      |x      |1
A'.B    |x      |x      |x      |1
A.B     |x      |x      |x      |x
A.B'    |x      |x      |1      |x
```

# Cache Visualizer
This is a cache visualizer tool dedicated just to solve most of the CS2100 cache problem. Therefore, the storage of each cache block count in words instead of bytes.

## Input format

1. Select the Cache Type
2. Input the number of words in each cache block
3. Input the total number of words in the cache memory
4. Input the number of block in a set (input 1 if it is a direct mapped cache)
5. Input number of array in memory
6. Input address of the arrays (must be in hexadecimal)
7. Memory Access

Example

This means loading `A[0]` into the cache with the respective order
```
Memory Access : A[0]
```

This means loading `B[0],A[30]` into the cache with the respective order
```
Memory Access : B[0] A[30]
```

This means loading `A[0],A[1],A[2],...,A[30],B[30]` into the cache with the respective order
```
Memory Access : A[0-30] B[30]
```

This means loading `A[0],A[1],A[2],...,A[30],B[2],C[3],C[4],C[5]` into the cache with the respective order
```
Memory Access : A[0-30] B[2] C[3-5]
```

### Example

```
Select Cache Type (Input the row number):
 1. Least Recently Used (LRU)
 2. First in First out (FIFO)
 3. Least Frequently Used (LFU)
1
Number of words in a cache block : 4
Total number of words in cache memory : 64
Number of block in a set : 2
------------------------------
Offset : 4
Set/block index : 3
------------------------------
Number of array in memory : 2
Address of array A : 0x00000000
Address of array B : 0x03ffff00
------------------------------
Memory access : A[0]
------------------------------
Accessing 0, 0x00000000
Tag : 0, 0x00000000
Index : 0, 0x00000000
Offset : 0, 0x00000000
Time : 1
It is a miss...

                        ||Block 0                 ||Block 1
0                       ||A[0],A[1],A[2],A[3]     ||
1                       ||                        ||
2                       ||                        ||
3                       ||                        ||
4                       ||                        ||
5                       ||                        ||
6                       ||                        ||
7                       ||                        ||
Hit rate for array A : 0/1
Hit rate for array B : 0/0
------------------------------
input 'C' to clear cache
input 'Q' to quit
Memory access : B[0] A[2]
------------------------------
Accessing 67108608, 0x03ffff00
Tag : 524286, 0x0007fffe
Index : 0, 0x00000000
Offset : 0, 0x00000000
Time : 2
It is a miss...

------------------------------
Accessing 8, 0x00000008
Tag : 0, 0x00000000
Index : 0, 0x00000000
Offset : 8, 0x00000008
Time : 2
HIT!!!

                        ||Block 0                 ||Block 1
0                       ||A[0],A[1],A[2],A[3]     ||B[0],B[1],B[2],B[3]
1                       ||                        ||
2                       ||                        ||
3                       ||                        ||
4                       ||                        ||
5                       ||                        ||
6                       ||                        ||
7                       ||                        ||
Hit rate for array A : 1/2
Hit rate for array B : 0/1
------------------------------
input 'C' to clear cache
input 'Q' to quit
```
