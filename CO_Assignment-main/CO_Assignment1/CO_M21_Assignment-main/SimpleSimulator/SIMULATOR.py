# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:40:54 2021

@author: Shrugal Tayal
"""
#Printing Function
import matplotlib.pyplot as plt
def printo(reg):
    print(('0'*(8-len((bin(pc))[(bin(pc)).index('b')+1:]))+(bin(pc))[(bin(pc)).index('b')+1:]) + " " +
          ('0'*(16-len((bin(reg['000']))[(bin(reg['000'])).index('b')+1:]))+(bin(reg['000']))[(bin(reg['000'])).index('b')+1:]) + " " +
          ('0'*(16-len((bin(reg['001']))[(bin(reg['001'])).index('b')+1:]))+(bin(reg['001']))[(bin(reg['001'])).index('b')+1:]) + " " +
          ('0'*(16-len((bin(reg['010']))[(bin(reg['010'])).index('b')+1:]))+(bin(reg['010']))[(bin(reg['010'])).index('b')+1:]) + " " +
          ('0'*(16-len((bin(reg['011']))[(bin(reg['011'])).index('b')+1:]))+(bin(reg['011']))[(bin(reg['011'])).index('b')+1:]) + " " +
          ('0'*(16-len((bin(reg['100']))[(bin(reg['100'])).index('b')+1:]))+(bin(reg['100']))[(bin(reg['100'])).index('b')+1:]) + " " +
          ('0'*(16-len((bin(reg['101']))[(bin(reg['101'])).index('b')+1:]))+(bin(reg['101']))[(bin(reg['101'])).index('b')+1:]) + " " +
          ('0'*(16-len((bin(reg['110']))[(bin(reg['110'])).index('b')+1:]))+(bin(reg['110']))[(bin(reg['110'])).index('b')+1:]) + " " +
          '0' * 12 + reg['111'])

# __functions__
def add(opcode, reg, code, pc):  # 1
    # type A
    reg['111'] = "0000"
    reg1 = reg[code[7:10]]
    reg2 = reg[code[10:13]]
    reg3 = reg[code[13:]]
    sum = reg2 + reg3
    if sum < 0 or sum > 255:
        reg['111'] = '1000'
    elif sum >= 0 and sum <= 255:
        reg[code[7:10]] = sum
    printo(reg)

def sub(opcode, reg, code, pc):  # 2
    # type A
    reg['111'] = "0000"
    reg1 = reg[code[7:10]]
    reg2 = reg[code[10:13]]
    reg3 = reg[code[13:]]
    diff = reg2 - reg3
    if diff < 0 or diff > 255:
        reg['111'] = '1000'
        reg[code[7:10]] = 0
    elif diff >= 0 and diff <= 255:
        reg[code[7:10]] = diff
    printo(reg)

def movi(opcode, reg, code, pc):  # 3
    # typeB
    reg['111'] = "0000"
    imm = int(code[8:], 2)
    reg[code[5:8]] = imm
    printo(reg)

def move(opcode, reg, code, pc):  # 4
    # type C
    if code[13:] == "111":
        reg[code[10:13]] = int(reg[code[13:]], 2)
        reg['111'] = '0000'
    elif code[13:] != "111":
        reg[code[10:13]] = reg[code[13:]]
    printo(reg)

def load(opcode, reg, code, pc, var): #5
    #typeD
    reg['111'] = "0000"
    reg1 = reg[code[5:8]]
    memadrr = code[8:]
    mem=int(str(memaddr),2)
    reg[5:8] = mem
    printo(reg)

def stor(opcode, reg, code, pc, var):  # 6
    # type D
    reg['111'] = "0000"
    reg1 = reg[code[5:8]]
    reg1 = bin(reg1).replace("0b", (16 - len(bin(reg1)[2:])) * '0')
    var.append(reg1)
    printo(reg)

def mul(opcode, reg, code, pc):  # 7
    # type A
    reg['111'] = "0000"
    reg1 = reg[code[7:10]]
    reg2 = reg[code[10:13]]
    reg3 = reg[code[13:]]
    pro = reg2 * reg3
    if pro < 0 or pro > 255:
        reg['111'] = '1000'
        reg[code[7:10]] = 0
    elif pro >= 0 and pro <= 255:
        reg[code[7:10]] = pro
    printo(reg)

def div(opcode, reg, code, pc):      #8
    #type C
    reg['111'] = "0000"
    reg1 = reg[code[10:13]]
    reg2 = reg[code[13:]]
    if reg2 != 0:
        quo = reg1/reg2
        reg[code[10:13]] =quo
    printo(reg)

def rightshift(opcode, reg, code, pc):  # 9
    # type B
    reg['111'] = "0000"
    reg1 = reg[code[5:8]]
    imm = code[8:]
    imm = int(imm, 2)
    result = reg1 >> imm
    if result < 0 or result > 255:
        reg['111'] = '1001'
        reg[code[5:8]] = 0
    elif result >= 0 and result <= 255:
        reg[code[5:8]] = result
    printo(reg)

def leftshift(opcode, reg, code, pc):  # 10
    # type B
    reg['111'] = "0000"
    reg1 = reg[code[5:8]]
    imm = code[8:]
    imm = int(imm, 2)
    result = reg1 << imm
    if result < 0 or result > 255:
        reg['111'] = '1000'
        reg[code[5:8]] = 0
    elif result >= 0 and result <= 255:
        reg[code[5:8]] = result
    printo(reg)

def exor(opcode, reg, code, pc):  # 11
    # type A
    reg['111'] = "0000"
    reg1 = reg[code[7:10]]
    reg2 = reg[code[10:13]]
    reg3 = reg[code[13:]]
    x = reg2 ^ reg3
    reg[code[7:10]] = x
    printo(reg)

def bitor(opcode, reg, code, pc):  # 12
    # type A
    reg['111'] = "0000"
    reg1 = reg[code[7:10]]
    reg2 = reg[code[10:13]]
    reg3 = reg[code[13:]]
    result = reg2 | reg3
    if result < 0 or result > 255:
        reg['111'] = '1000'
        reg[code[7:10]] = 0
    elif result >= 0 and result <= 255:
        reg[code[7:10]] = result
    printo(reg)

def bitand(opcode, reg, code, pc):  # 13
    # type A
    reg['111'] = "0000"
    reg1 = reg[code[7:10]]
    reg2 = reg[code[10:13]]
    reg3 = reg[code[13:]]
    result = reg2 & reg3
    if result < 0 or result > 255:
        reg['111'] = '1000'
        reg[code[7:10]] = 0
    elif result >= 0 and result <= 255:
        reg[code[7:10]] = result
    printo(reg)

def bitnot(opcode, reg, code, pc):  # 14
    # type C
    reg['111'] = "0000"
    reg1 = reg[code[10:13]]
    reg2 = reg[code[13:]]
    result = ~reg2
    if result < 0 or result > 255:
        reg['111'] = '1000'
        reg[code[10:13]] = 0
    elif result >= 0 and result <= 255:
        reg[code[10:13]] = result
    printo(reg)

def cmp(opcode, reg, code, pc):  # 15
    # type C
    reg['111'] = "0000"
    reg1 = reg[code[10:13]]
    reg2 = reg[code[13:]]
    if reg1 > reg2:
        reg['111'] = "0010"

    if reg1 < reg2:
        reg['111'] = "0100"

    if reg1 == reg2:
        reg['111'] = "0001"
    printo(reg)

def unjump(opcode, reg, code, pc):  # infinity loop to be decided   #16
    # type E
    reg['111'] = "0000"
    printo(reg)

def jmpiflt(opcode, reg, code, pc):  # 17
    # type E
    reg['111'] = '0000'
    printo(reg)

def jmpifgrt(opcode, reg, code, pc):  # 18
    # type E
    reg['111'] = '0000'
    printo(reg)

def jmpifeq(opcode, reg, code, pc):  # 19
    # type E
    reg['111'] = '0000'
    printo(reg)

def hlt(opcode, code, pc):  # 20
    # type F
    reg['111'] = "0000"
    printo(reg)

# __main__
if __name__ == "__main__":

    from sys import stdin
    inst = []
    for line in stdin:
        if line == "":
            break
        else:
            line = line.split()
            for i in range(len(line)):
                line[i].strip()
            inst.append(line)

#     code = '''0001000100000100
# 0001001000000100
# 0111000000001010
# 0001100000011111
# 0001010000000001
# 0111000000011100
# 1000100000000111
# 1001100000000000'''
#     code = code.split('\n')
#     inst = []
#     for i in code:
#         inst.append(i.split())

# storage
opcode = ( "00000", "00001", "00010", "00011","00100", "00101", "00110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011")
reg = {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': '0000'}
var = []

# execute
for pc in range(len(inst)):
    code = inst[pc][0]
    op = code[0:5]
    if op in opcode:
        if op == "00000":
            add(opcode, reg, code, pc)
        if op == "00001":
            sub(opcode, reg, code, pc)
        if op == "00010":
            movi(opcode, reg, code, pc)
        if op == "00011":
            move(opcode, reg, code, pc)
        if op == "00100":
            load(opcode, reg, code, pc, var)
        if op == "00101":
            stor(opcode, reg, code, pc, var)
        if op == "00110":
            mul(opcode, reg, code, pc)
        if op == "00111":
            div(opcode, reg, code, pc)
        if op == "01000":
            rightshift(opcode, reg, code, pc)
        if op == "01001":
            leftshift(opcode, reg, code, pc)
        if op == "01010":
            exor(opcode, reg, code, pc)
        if op == "01011":
            bitor(opcode, reg, code, pc)
        if op == "01100":
            bitand(opcode, reg, code, pc)
        if op == "01101":
            bitnot(opcode, reg, code, pc)
        if op == "01110":
            cmp(opcode, reg, code, pc)
        if op == "01111":
            unjump(opcode, reg, code, pc)
            memadrr = code[8:]
            memadrr = int(memadrr, 2)
            pc = memadrr
        if op == "10000":
            jmpiflt(opcode, reg, code, pc)
            if (reg['111'][1] == '1'):
                memadrr = code[8:]
                memadrr = int(memadrr, 2)
                pc = memadrr
        if op == "10001":
            jmpifgrt(opcode, reg, code, pc)
            if (reg['111'][2] == '1'):
                memadrr = code[8:]
                memadrr = int(memadrr, 2)
                pc = memadrr
        if op == "10010":
            jmpifeq(opcode, reg, code, pc)
            if (reg['111'][3] == '1'):
                memadrr = code[8:]
                memadrr = int(memadrr, 2)
                pc = memadrr
        if op == "10011":
            hlt(opcode, code, pc)


# memory dump
mem_address=[]
cycle=[]
for i in range(len(inst)):
  cycle.append(i)
mem_count = len(inst) + len(var)
#print(mem_count)
for i in range(len(inst)):
    mem_address.append(inst[i][0])
    print(inst[i][0])
if len(var)>0:
    for i in var:
        #mem_address.append(i)
        print(i)
mem_left = 256 - mem_count
for i in range(mem_left):
    print("0000000000000000")


plt.scatter(cycle, mem_address)
plt.show()
# print(cycle)
# print(mem_address)
