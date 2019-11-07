from __future__ import print_function

s0=[0x3e,0x72,0x5b,0x47,0xca,0xe0,0x00,0x33,0x04,0xd1,0x54,0x98,0x09,0xb9,0x6d,0xcb,
    0x7b,0x1b,0xf9,0x32,0xaf,0x9d,0x6a,0xa5,0xb8,0x2d,0xfc,0x1d,0x08,0x53,0x03,0x90,
    0x4d,0x4e,0x84,0x99,0xe4,0xce,0xd9,0x91,0xdd,0xb6,0x85,0x48,0x8b,0x29,0x6e,0xac,
    0xcd,0xc1,0xf8,0x1e,0x73,0x43,0x69,0xc6,0xb5,0xbd,0xfd,0x39,0x63,0x20,0xd4,0x38,
    0x76,0x7d,0xb2,0xa7,0xcf,0xed,0x57,0xc5,0xf3,0x2c,0xbb,0x14,0x21,0x06,0x55,0x9b,
    0xe3,0xef,0x5e,0x31,0x4f,0x7f,0x5a,0xa4,0x0d,0x82,0x51,0x49,0x5f,0xba,0x58,0x1c,
    0x4a,0x16,0xd5,0x17,0xa8,0x92,0x24,0x1f,0x8c,0xff,0xd8,0xae,0x2e,0x01,0xd3,0xad,
    0x3b,0x4b,0xda,0x46,0xeb,0xc9,0xde,0x9a,0x8f,0x87,0xd7,0x3a,0x80,0x6f,0x2f,0xc8,
    0xb1,0xb4,0x37,0xf7,0x0a,0x22,0x13,0x28,0x7c,0xcc,0x3c,0x89,0xc7,0xc3,0x96,0x56,
    0x07,0xbf,0x7e,0xf0,0x0b,0x2b,0x97,0x52,0x35,0x41,0x79,0x61,0xa6,0x4c,0x10,0xfe,
    0xbc,0x26,0x95,0x88,0x8a,0xb0,0xa3,0xfb,0xc0,0x18,0x94,0xf2,0xe1,0xe5,0xe9,0x5d,
    0xd0,0xdc,0x11,0x66,0x64,0x5c,0xec,0x59,0x42,0x75,0x12,0xf5,0x74,0x9c,0xaa,0x23,
    0x0e,0x86,0xab,0xbe,0x2a,0x02,0xe7,0x67,0xe6,0x44,0xa2,0x6c,0xc2,0x93,0x9f,0xf1,
    0xf6,0xfa,0x36,0xd2,0x50,0x68,0x9e,0x62,0x71,0x15,0x3d,0xd6,0x40,0xc4,0xe2,0x0f,
    0x8e,0x83,0x77,0x6b,0x25,0x05,0x3f,0x0c,0x30,0xea,0x70,0xb7,0xa1,0xe8,0xa9,0x65,
    0x8d,0x27,0x1a,0xdb,0x81,0xb3,0xa0,0xf4,0x45,0x7a,0x19,0xdf,0xee,0x78,0x34,0x60
]

s1=[0x55,0xc2,0x63,0x71,0x3b,0xc8,0x47,0x86,0x9f,0x3c,0xda,0x5b,0x29,0xaa,0xfd,0x77,
	0x8c,0xc5,0x94,0x0c,0xa6,0x1a,0x13,0x00,0xe3,0xa8,0x16,0x72,0x40,0xf9,0xf8,0x42,
	0x44,0x26,0x68,0x96,0x81,0xd9,0x45,0x3e,0x10,0x76,0xc6,0xa7,0x8b,0x39,0x43,0xe1,
	0x3a,0xb5,0x56,0x2a,0xc0,0x6d,0xb3,0x05,0x22,0x66,0xbf,0xdc,0x0b,0xfa,0x62,0x48,
	0xdd,0x20,0x11,0x06,0x36,0xc9,0xc1,0xcf,0xf6,0x27,0x52,0xbb,0x69,0xf5,0xd4,0x87,
	0x7f,0x84,0x4c,0xd2,0x9c,0x57,0xa4,0xbc,0x4f,0x9a,0xdf,0xfe,0xd6,0x8d,0x7a,0xeb,
	0x2b,0x53,0xd8,0x5c,0xa1,0x14,0x17,0xfb,0x23,0xd5,0x7d,0x30,0x67,0x73,0x08,0x09,
	0xee,0xb7,0x70,0x3f,0x61,0xb2,0x19,0x8e,0x4e,0xe5,0x4b,0x93,0x8f,0x5d,0xdb,0xa9,
	0xad,0xf1,0xae,0x2e,0xcb,0x0d,0xfc,0xf4,0x2d,0x46,0x6e,0x1d,0x97,0xe8,0xd1,0xe9,
	0x4d,0x37,0xa5,0x75,0x5e,0x83,0x9e,0xab,0x82,0x9d,0xb9,0x1c,0xe0,0xcd,0x49,0x89,
	0x01,0xb6,0xbd,0x58,0x24,0xa2,0x5f,0x38,0x78,0x99,0x15,0x90,0x50,0xb8,0x95,0xe4,
	0xd0,0x91,0xc7,0xce,0xed,0x0f,0xb4,0x6f,0xa0,0xcc,0xf0,0x02,0x4a,0x79,0xc3,0xde,
	0xa3,0xef,0xea,0x51,0xe6,0x6b,0x18,0xec,0x1b,0x2c,0x80,0xf7,0x74,0xe7,0xff,0x21,
	0x5a,0x6a,0x54,0x1e,0x41,0x31,0x92,0x35,0xc4,0x33,0x07,0x0a,0xba,0x7e,0x0e,0x34,
	0x88,0xb1,0x98,0x7c,0xf3,0x3d,0x60,0x6c,0x7b,0xca,0xd3,0x1f,0x32,0x65,0x04,0x28,
	0x64,0xbe,0x85,0x9b,0x2f,0x59,0x8a,0xd7,0xb0,0x25,0xac,0xaf,0x12,0x03,0xe2,0xf2,
]

DDT=[[0 for i in range(256)] for i in range(256)]
LAT=[[0 for i in range(256)] for i in range(256)]

def int2bin(x):                                   #将数字转为二进制形式
    binx = bin(x)[2:]                             #去掉前面的"0x"，位数小于8时，添0补足
    if len(binx) < 8:
        binx = "0"*(8-len(binx)) + binx
    return binx


def get_DDT(SBoxes):
    for x in range(256):                         #x=x'^x''
        result = []
        for x1 in range (256):
            for x2 in range (256):
                if x1 ^ x2 == x:                 #对于某固定的x,通过遍历得到满足x=x'^x''明文对
                   result.append((x1,x2))
                   break
        for t in result:
            diff = SBoxes[t[0]] ^ SBoxes[t[1]]   #通过S盒置换，得到x'、x''对应的输出y'^y''，计算异或值 diff=y'^y''
            DDT[x][diff] += 1                    #记录输入为x'、x''时结果为diff的次数
    return DDT


def get_LAT( SBoxes):
    for i in range(256):                        #遍历
        for j in range(256):
            count= 0
            for x in range(256):
                y =SBoxes[x]
                count+= fun(i,x,j,y)             #计数
            count=128-count
            LAT[i][j]=count                       #将遍历结果存入LAT表中
    # print("finish")
    return LAT


def fun(i,x,j,y):                                #按位异或
    bini=int2bin(i)
    binx=int2bin(x)
    binj=int2bin(j)
    biny=int2bin(y)

    t1= int(bini[0]) & int(binx[0])
    t2= int(binj[0]) & int(biny[0])
    for k in range(1,8):
        t1 ^= int(bini[k]) & int(binx[k])
        t2 ^= int(binj[k]) & int(biny[k])

    return t1^t2

def saveTable(table,filename):                   #将结果存入TXT文件中
    file= open(filename, 'w')
    for fp in table:
        file.write(str(fp))
        file.write('\n')



def printTable(table):                           #打印
    print("\t|"+"   0",end='')
    for i in range(1, 10):                       #按数字位数添加空格，以对齐数字
        print("\t"+"   "+str(i), end='')
    for i in range(10, 100):
        print("\t"+"  "+str(i), end='')
    for i in range(100, 256):
        print("\t"+" "+str(i), end='')
    print()
    for i in range(0, 256):
        print("--------",end='')
    print()
    for k  in range(len(table)):
        s= str(k) + "\t|"
        for i in table[k]:
            s = s + "   " + str(i) + "\t"
        print (s)


#printDDT(get_DDT(s0))
#printTable(get_LAT(s0))

if __name__ == "__main__":

    T1=get_DDT(s0)
    saveTable(T1,"DDT1.txt")

    T2=get_DDT(s1)
    saveTable(T2,"DDT2.txt")

    T3=get_LAT(s0)
    saveTable(T3,"LAT1.txt")

    T4=get_LAT(s1)
    saveTable(T4,"LAT2.txt")

    print("DDT(s0):")
    printTable(T1)
    print("DDT(s1):")
    printTable(T2)
    print("LAT(S0):")
    printTable(T3)
    print("LAT(S1):")
    printTable(T4)
