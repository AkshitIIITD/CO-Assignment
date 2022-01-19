# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:43:39 2021

@author: Shrugal Tayal
"""
#__functions__:
def addn(x,flag,rega):
    # type A
    flag='0000'
    sum=rega[x[2]][1]+rega[x[3]][1]
    if sum > 255:
        flag='1000'
        return 'Error: overflow detected'
    else:
        s = opcode[x[0]]+'0'*2+rega[x[1]][0]+rega[x[2]][0]+rega[x[3]][0]
        rega[x[1]][1]=sum
        b = str(bin(sum))
        slice = b.index('b')
        b = b[slice+1:]
        b = '0'*(16-len(b))+b
        rega[x[1]][2]=b
        return s

def subt(x,flag,rega):
    # type A
    flag='0000'
    dif=rega[x[2]][1]-rega[x[3]][1]
    if dif < 0:
        flag='1000'
        rega[x[1]][1]=0
        return 'Error: overflow detected'
    else:
        s = opcode[x[0]]+'0'*2+rega[x[1]][0]+rega[x[2]][0]+rega[x[3]][0]
        rega[x[1]][1]=dif
        b = str(bin(dif))
        slice = b.index('b')
        b = b[slice+1:]
        b = '0'*(16-len(b))+b
        rega[x[1]][2]=b
        return s

def move(x,flag,rega):
    if '$' in x[2]: # type B
        a = int(x[2][1:])
        rega[x[1]][1]=a
        b = str(bin(a))    
        slice = b.index('b')
        b = b[slice+1:]
        a = '0'*(16-len(b))+b
        rega[x[1]][2]=a
        b = '0'*(8-len(b))+b
        s = opcode[x[0]][0]+rega[x[1]][0]+b
        return s
    else:   # type C
        s = opcode[x[0]][1]+'0'*5+rega[x[1]][0]+rega[x[2]][0]
        if x[2] != 'FLAGS':
            rega[x[1]][1]=rega[x[2]][1]
            rega[x[1]][2]=rega[x[2]][2]
        if x[2] == 'FLAGS':
            rega[x[1]][1]=int(rega[x[2]][1])
        return s
    
def load(x,flag,rega,var):
    val=var[x[2]]
    memaddr=format(val ,'08b')
    s = opcode[x[0]] + rega[x[1]][0] + memaddr
    return s
    
def store(x,flag,rega):
    val=var[x[2]]
    memaddr=format(val ,'08b')
    s = opcode[x[0]] + rega[x[1]][0] + memaddr
    return s

def mult(x,flag,rega):
    # type A
    flag='0000'
    pro=rega[x[2]][1]*rega[x[3]][1]
    if pro > 255:
        flag='1000'
        return 'Error: overflow detected'
    else:
        s = opcode[x[0]]+'0'*2+rega[x[1]][0]+rega[x[2]][0]+rega[x[3]][0]
        rega[x[1]][1]=pro
        b = str(bin(pro))
        slice = b.index('b')
        b = b[slice+1:]
        b = '0'*(16-len(b))+b
        rega[x[1]][2]=b
        return s 

def divn(x,flag,rega):
    # type C
    if rega[x[2]][1]!=0:
        q=int(rega[x[1]][1]//rega[x[2]][1])
        r=int(rega[x[1]][1]%rega[x[2]][1])
        rega['R1'][1]=r
        b = str(bin(r))
        slice = b.index('b')
        b = b[slice+1:]
        b = '0'*(16-len(b))+b
        rega['R1'][2]=b
        rega['R0'][1]=q
        b = str(bin(q))
        slice = b.index('b')
        b = b[slice+1:]
        b = '0'*(16-len(b))+b
        rega['R0'][2]=b
    s = opcode[x[0]]+'0'*5+rega[x[1]][0]+rega[x[2]][0]
    return s 

def right(x,flag,rega):
    # type B
    m = rega[x[1]][1]
    n = int(x[2][1:])
    a = m>>n
    if a<1:
        return 'Error: overflow detected'
    else:
        rega[x[1]][1]=a
        b=str(bin(a))
        slice = b.index('b')
        b = b[slice+1:]
        a = '0'*(16-len(b))+b
        rega[x[1]][2]=a
        b = '0'*(8-len(b))+b
        s = opcode[x[0]]+rega[x[1]][0]+b
        return s
    
def left(x,flag,rega):
    # type B
    m = rega[x[1]][1]
    n = int(x[2][1:])
    a = m<<n
    if a>255:
        return 'Error: overflow detected'
    else:
        rega[x[1]][1]=a
        b=str(bin(a))
        slice = b.index('b')
        b = b[slice+1:]
        a = '0'*(16-len(b))+b
        rega[x[1]][2]=a
        b = '0'*(8-len(b))+b
        s = opcode[x[0]]+rega[x[1]][0]+b
        return s

def exor(x,flag,rega):
    # type A
    m = rega[x[2]][1]
    n = rega[x[3]][1]
    a = m^n     # cross check
    rega[x[1]][1] = a
    b = str(bin(a))
    slice = b.index('b')
    b = b[slice+1:]
    b = '0'*(16-len(b))+b
    rega[x[1]][2]=b
    s = opcode[x[0]]+'0'*2+rega[x[1]][0]+rega[x[2]][0]+rega[x[3]][0]
    return s

def Or(x,flag,rega):
    # type A
    m = rega[x[2]][1]
    n = rega[x[3]][1]
    a = m|n     # cross check
    rega[x[1]][1] = a
    b = str(bin(a))
    slice = b.index('b')
    b = b[slice+1:]
    b = '0'*(16-len(b))+b
    rega[x[1]][2]=b
    s = opcode[x[0]]+'0'*2+rega[x[1]][0]+rega[x[2]][0]+rega[x[3]][0]
    return s

def And(x,flag,rega):
    # type A
    m = rega[x[2]][1]
    n = rega[x[3]][1]
    a = m&n     # cross check
    rega[x[1]][1] = a
    b = str(bin(a))
    slice = b.index('b')
    b = b[slice+1:]
    b = '0'*(16-len(b))+b
    rega[x[1]][2]=b
    s = opcode[x[0]]+'0'*2+rega[x[1]][0]+rega[x[2]][0]+rega[x[3]][0]
    return s

def inv(x,flag,rega):
    # type C
    m = rega[x[2]][1]
    a = ~m     # cross check
    rega[x[1]][1] = a
    b = str(bin(a))
    slice = b.index('b')
    b = b[slice+1:]
    b = '0'*(16-len(b))+b
    rega[x[1]][2]=b
    s = opcode[x[0]]+'0'*5+rega[x[1]][0]+rega[x[2]][0]
    return s

def comp(x,flag,rega):
    # type C
    flag='0000'
    val1=rega[x[1]][1]
    val2=rega[x[2]][1]
    if(val1<val2):
      flag='0100'
    elif(val1>val2):
      flag='0010'
    else:
      flag='0001'
    s = opcode[x[0]]+'0'*5+rega[x[1]][0]+rega[x[2]][0]
    return s

def jump(x,flag,label):
    #type E
    addr=x[1]
    val = label[addr]
    memaddr=format(val ,'08b')
    s = opcode[x[0]] + '0'*3 + memaddr
    return s

def jumpiflt(x,flag,rega,label):
    # type E
    addr=x[1]
    val=label[addr]
    b = str(bin(val))
    slice = b.index('b')
    b = b[slice+1:]
    b = '0'*(8-len(b))+b
    s=opcode[x[0]]+'0'*3+b
    return s

def jumpifgrt(x,flag,rega,label):
    # type E
    addr=x[1]
    val=label[addr]
    b = str(bin(val))
    slice = b.index('b')
    b = b[slice+1:]
    b = '0'*(8-len(b))+b
    s=opcode[x[0]]+'0'*3+b
    return s

def jumpifeq(x,flag,rega,label):
    # type E
    addr=x[1]
    val=label[addr]
    b = str(bin(val))
    slice = b.index('b')
    b = b[slice+1:]
    b = '0'*(8-len(b))+b
    s=opcode[x[0]]+'0'*3+b
    return s

def halt(x):
    # type F
    if x[0] == 'hlt':
        s = opcode[x[0]]+'0'*11
        return False,s

# __main__:
if __name__ == "__main__" :
     # To be updated later
    f=open('tests.txt','r')
    code=f.read()
    code = code.split('\n')
    inst = []
    for i in code:
        inst.append(i.split())
        
    #variable handling
    var={}
    noofvar=0
    for i in inst:
      if(i[0]=='var'):
        noofvar+=1
        var[i[1]]=-1
      else:
        break
    varaddressstart=len(inst)-noofvar
    k=varaddressstart
    for j in var:
      var[j]= k
      k+=1

    #variable handling ends

    bincode = []    # stores the assembled code
    # predefined
    opcode = {'add':'00000','sub':'00001','mov':('00010','00011'),'ld':'00100','st':'00101',
              'mul':'00110','div':'00111','rs':'01000','ls':'01001','xor':'01010','or':'01011',
              'and':'01100','not':'01101','cmp':'01110','jmp':'01111','jlt':'10000','jgt':'10001','je':'10010','hlt':'10011'}
    
    flag = '0000'   # V, L, G, E 
    rega = {'R0':['000',0,''],'R1':['001',0,''],'R2':['010',0,''],'R3':['011',0,''],
             'R4':['100',0,''],'R5':['101',0,''],'R6':['110',0,''],'FLAGS':['111',flag]}
    # Registers will have values as integers
    label={}

    val = []
    check = True
    linenumber=-1
    
    for i in range(len(inst)):
        if check == False:
            break
        if(inst[i][0]=='var'):
          # var[inst[i][1]]=
          continue
        if ':' in inst[i][0]: # it is a label
          l = inst[i][0][:-1]  
          linenumber+=1
          label[l]=linenumber
        if (inst[i][0] in opcode):
          linenumber+=1
    
    linenumber=-1
    for i in range(len(inst)):
      if check == False:
            break
      if(inst[i][0]=='var'):
          # var[inst[i][1]]=
          continue
      if ':' in inst[i][0]: # it is a label
          linenumber+=1
          l = inst[i][0][:-1]
          label[l]=linenumber
          x = inst[i][1:]          
          if x[0] in opcode:
              if x[0] == 'add':
                  bincode.append(addn(x,flag,rega))
              if x[0] == 'sub':
                  bincode.append(subt(x,flag,rega))
              if x[0] == 'mov':
                  bincode.append(move(x,flag,rega))
              if x[0] == 'ld':  # incomplete
                  bincode.append(load(x,flag,rega,var))
              if x[0] == 'st':  # incomplete
                  bincode.append(store(x,flag,rega))
              if x[0] == 'mul':
                  bincode.append(mult(x,flag,rega))
              if x[0] == 'div':
                  bincode.append(divn(x,flag,rega))
              if x[0] == 'rs':
                  bincode.append(right(x,flag,rega))
              if x[0] == 'ls':
                  bincode.append(left(x,flag,rega))
              if x[0] == 'xor':
                  bincode.append(exor(x,flag,rega))
              if x[0] == 'or':
                  bincode.append(Or(x,flag,rega))
              if x[0] == 'and':
                  bincode.append(And(x,flag,rega))
              if x[0] == 'not': # To be checked
                  bincode.append(inv(x,flag,rega))
              if x[0] == 'cmp': # To be checked
                  bincode.append(comp(x,flag,rega))
              if x[0] == 'jmp': # To be checked
                  bincode.append(jump(x,flag,label))      
              if x[0] == 'jlt': # To be checked
                  bincode.append(jumpiflt(x,flag,rega,label))  
              if x[0] == 'jgt': # To be checked
                  bincode.append(jumpifgrt(x,flag,rega,label))      
              if x[0] == 'je': # To be checked
                  bincode.append(jumpifeq(x,flag,rega,label))      
              if x[0] == 'hlt':
                  check,s = halt(x) 
                  bincode.append(s)
      if (inst[i][0] in opcode):
          linenumber+=1
      if inst[i][0] in opcode:
          if inst[i][0] == 'add':
              bincode.append(addn(inst[i],flag,rega))
          if inst[i][0] == 'sub':
              bincode.append(subt(inst[i],flag,rega))
          if inst[i][0] == 'mov':
              bincode.append(move(inst[i],flag,rega))
          if inst[i][0] == 'ld':  # incomplete
              bincode.append(load(inst[i],flag,rega,var))
          if inst[i][0] == 'st':  # incomplete
              bincode.append(store(inst[i],flag,rega))
          if inst[i][0] == 'mul':
              bincode.append(mult(inst[i],flag,rega))
          if inst[i][0] == 'div':
              bincode.append(divn(inst[i],flag,rega))
          if inst[i][0] == 'rs':
              bincode.append(right(inst[i],flag,rega))
          if inst[i][0] == 'ls':
              bincode.append(left(inst[i],flag,rega))
          if inst[i][0] == 'xor':
              bincode.append(exor(inst[i],flag,rega))
          if inst[i][0] == 'or':
              bincode.append(Or(inst[i],flag,rega))
          if inst[i][0] == 'and':
              bincode.append(And(inst[i],flag,rega))
          if inst[i][0] == 'not': # To be checked
              bincode.append(inv(inst[i],flag,rega))
          if inst[i][0] == 'cmp': # To be checked
              bincode.append(comp(inst[i],flag,rega))
          if inst[i][0] == 'jmp': # To be checked
              bincode.append(jump(inst[i],flag,label))      
          if inst[i][0] == 'jlt': # To be checked
              bincode.append(jumpiflt(inst[i],flag,rega,label))  
          if inst[i][0] == 'jgt': # To be checked
              bincode.append(jumpifgrt(inst[i],flag,rega,label))      
          if inst[i][0] == 'je': # To be checked
              bincode.append(jumpifeq(inst[i],flag,rega,label))      
          if inst[i][0] == 'hlt':
               check,s = halt(inst[i]) 
               bincode.append(s)
    
#print(rega)
#print(bincode)
#print(flag)
for i in bincode:
     print(i)
#print(label)
#print(var)
#print(len(bincode))