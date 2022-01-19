#__functions__:


###### FINAL SAVE

'''I tried to implement errors as per given instructions in assignment but currently there are a few bugs in this code..... this code is not for assessment previously commited is'''
######  
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
        return True,s

# __main__:
if __name__ == "__main__" :
     # To be updated later
    from sys import stdin
    inst = []
    for line in stdin:
        if line == '':
            break
        else:
            line=line.split()
            for i in range(len(line)):
                line[i].strip()
            inst.append(line)  

#     code='''mov R1 R2
# mov R1 R2
# mov R1 R2
# mov R1 R2
# mov R1 R2
# mov R1 R2
# hlt'''   
#     code = code.split('\n')
#     inst = []
#     for i in code:
#         inst.append(i.split())  


    #####general use functions
    def legalinst(s):# s is a string of instruction name
      if(s in opcode):
        return True
      else:
        return False

    def makereglist(instruction):
      regininst=[]
      for i in instruction:
        if i in rega: ############
          regininst.append(i)
  
      return regininst

    def legalreg(reglist):
      for i in reglist:
        if i not in rega:
          return False
  
      return True

    def var_defined_un(v):
      if v not in var:
        return False
      else:
        return True

    def isvalidlabel(lab):
      if lab not in label:
        return False
      else:
        return True
# flag one pending

    def legalimmvalue(val):
      if (val<0 or val>255):
        return False
  
      else:
        return True

    def labelasvar(v):
      if var in label:
        return True
      else:
        return False

    def varaslabel(lab):
      if(lab in var):
        return True
      else:
        return False



    def typeofinstr(instruction):
      regcount=0
      varcount=0
      memadrresscount=0
      imme=0
      for i in instruction:
        if i in rega:
          regcount+=1

        if i in var:
          varcount+=1

        if i in label:
          memadrresscount+=1

        if '$' in i:
          imme+=1
      
      if (regcount==3 or instruction[0]=='add' or instruction[0]=='sub' or instruction[0]=='mul' or instruction[0]=='xor' or instruction[0]=='or' or instruction[0]=='and'):
          return 'A'
      if ((regcount==1 and imme==1) or instruction[0]=='rs' or instruction[0]=='ls'):
          return 'B'
      if (regcount==2 or instruction[0]=='not' or instruction[0]=='cmp'):
          return 'C'
      if ((regcount==1 and varcount==1) or instruction[0]=='ld' or instruction[0]=='st'):
          return 'D'
      if ((regcount==0 and memadrresscount==1) or instruction[0]=='jmp' or instruction[0]=='jgt' or instruction[0]=='je' or instruction[0]=='jlt'):
          return 'E'
      if (regcount==0 and varcount==0 and imme==0):
          return 'F'
    #variable handling
    var={}
    noofvar=0 
    # for i in inst:
    #   if(i[0]=='var'):
    #     noofvar+=1
    #     var[i[1]]=-1
    #   else:
    #     break
    haltpresent=False
    notnow = False
    errorflag= False
    linen=-1
    for i in inst: # hlt, var x
      linen+=1
      if (i[0]=='var'): #### hlt , var x
        pass
        if (notnow==True): # error g         
          errorflag=True
          print(str(linen)+" Variables not declared at the beginning")
          break
        else:
          noofvar+=1
          var[i[1]]=-1

      else:
        notnow = True


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
        #if check == False:
        #break
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
      if(errorflag):
        break
      if check == False:
            break
      if (inst[i][0]=='var'):
          # var[inst[i][1]]=
          continue
      if ':' in inst[i][0]: # it is a label
          linenumber+=1
          l = inst[i][0][:-1]
          label[l]=linenumber
          x = inst[i][1:]

          if(not (legalinst(inst[i][1]))): #error a
            errorflag=True
            print(str(linenumber)+' Typos in instruction name')
            break

          regininst=makereglist(inst[i])
          if (not (legalreg(regininst))): # error a
            errorflag=True
            print(str(linenumber)+' Typos in register name')
            break

          typeofinst=typeofinstr(x) # error c and f
          if (typeofinst=='E'):
              if x[1] not in label:
                  errorflag=True
                  print(str(linenumber)+' Use of undefined labels')
                  break

              if x[1] in var:
                  errorflag=True
                  print('Misuse of variables as labels')
                  break

          if (typeofinst=='B'): # error e
              val=x[2][1:]
              val=int (val)
              if(not (legalimmvalue(val))):
                  errorflag=True
                  print(str(linenumber)+' Illegal Immediate values')
                  break

          if x[0] in opcode:              

              if x[0] == 'add':
                  
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  if (typeofinst != 'A'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(addn(x,flag,rega))
              if x[0] == 'sub':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'A'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break

                  bincode.append(subt(x,flag,rega))
              if x[0] == 'mov':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  

                  movetyp=''
                  for y in x:
                    if '$' in i:
                      movetyp='immtype'
                    else:
                      movetyp='regtype'
                
                  if (movetyp=='immtype' and typeofinst!='B'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break

                  if (movetyp=='regtype' and typeofinst!='C'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break



                  bincode.append(move(x,flag,rega))

              if x[0] == 'ld':  # incomplete
                  if (not (var_defined_un(x[2]))): # error b 
                      errorflag=True
                      print(str(linenumber)+' Use of undefined variables')
                      break
                      

                  if (x[2] in labels): # error f
                      errorflag=True
                      print('Misuse of labels as variables')
                      break

                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'D'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break

                  bincode.append(load(x,flag,rega,var))
              if x[0] == 'st':
                  if (not (var_defined_un(x[2]))): #error b
                      errorflag=True
                      print(str(linenumber)+' Use of undefined variables')
                      break

                  if (x[2] in labels): # error f
                      errorflag=True
                      print('Misuse of labels as variables')
                      break

                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'D'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break

                  bincode.append(store(x,flag,rega))

              if x[0] == 'mul':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'A'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(mult(x,flag,rega))
              if x[0] == 'div':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  if (typeofinst != 'A'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(divn(x,flag,rega))

              if x[0] == 'rs':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'B'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(right(x,flag,rega))
              if x[0] == 'ls':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'B'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(left(x,flag,rega))
              if x[0] == 'xor':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  if (typeofinst != 'A'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(exor(x,flag,rega))
              if x[0] == 'or':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  if (typeofinst != 'A'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(Or(x,flag,rega))
              if x[0] == 'and':
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  if (typeofinst != 'A'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(And(x,flag,rega))
              if x[0] == 'not': # To be checked
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'C'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(inv(x,flag,rega))
              if x[0] == 'cmp': # To be checked
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'C'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(comp(x,flag,rega))
              if x[0] == 'jmp': # To be checked
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break

                  if (typeofinst != 'E'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(jump(x,flag,label))      
              if x[0] == 'jlt': # To be checked
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  if (typeofinst != 'E'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(jumpiflt(x,flag,rega,label))  
              if x[0] == 'jgt': # To be checked
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  if (typeofinst != 'E'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(jumpifgrt(x,flag,rega,label))      
              if x[0] == 'je': # To be checked
                  if (haltpresent==True):
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  if (typeofinst != 'E'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  bincode.append(jumpifeq(x,flag,rega,label))      
              if x[0] == 'hlt':
                  if (haltpresent==True): ####error i
                      errorflag=True
                      print(str(linenumber)+' hlt not being used as the last instruction')
                      break
                  haltpresent=True
                  if (typeofinst != 'F'):
                      errorflag=True
                      print(str(linenumber)+' Wrong syntax used for instructions')
                      break
                  check,s = halt(x) 
                  bincode.append(s)
      # if (inst[i][0] in opcode):
          

      
      
      if inst[i][0] in opcode:
          linenumber+=1
          if (not (legalinst(inst[i][0]))): # error a
                  errorflag=True
                  print(str(linenumber)+' Typos in instruction name')
                  break

          regininst=makereglist(inst[i])

          if (not (legalreg(regininst))): # error a
                  errorflag=True
                  print(str(linenumber)+' Typos in register name')
                  break

          typeofinst=typeofinstr(inst[i]) # error c and f
          if (typeofinst=='E'):
            if inst[i][1] not in label:
                  errorflag=True
                  print(str(linenumber)+' Use of undefined labels')
                  break

            if inst[i][1] in var:
                  errorflag=True
                  print('Misuse of variables as labels')
                  break

            if (typeofinst=='B'): # error e
              val=inst[i][2][1:]
              val=int (val)
              if(not (legalimmvalue(val))):
                  errorflag=True
                  print(str(linenumber)+' Illegal Immediate values')
                  break


          if inst[i][0] == 'add':
              
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break

              if (typeofinst != 'A'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break


              bincode.append(addn(inst[i],flag,rega))
          if inst[i][0] == 'sub':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break

              if (typeofinst != 'A'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break

              bincode.append(subt(inst[i],flag,rega))

          if inst[i][0] == 'mov':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              
              movetyp=''
              for y in inst[i]:
                if '$' in y:
                  movetyp='immtype'
                else:
                  movetyp='regtype'
              
              if (movetyp=='immtype' and typeofinst!='B'):
                  errorflag=True
                  print(str(linenumber)+' Wrong syntax used for instructions')
                  break

              if (movetyp=='regtype' and typeofinst!='C'):
                  errorflag=True
                  print(str(linenumber)+' Wrong syntax used for instructions')
                  break

              bincode.append(move(inst[i],flag,rega))

          if inst[i][0] == 'ld':  # incomplete
              if (not (var_defined_un(inst[i][2]))): #error b
                      errorflag=True
                      print(str(linenumber)+' Use of undefined variables')
                      break
              if (inst[i][2] in label): # error f
                      errorflag=True
                      print('Misuse of labels as variables')
                      break

              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'D'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(load(inst[i],flag,rega,var))
          if inst[i][0] == 'st':  # incomplete
              if (not (var_defined_un(inst[i][2]))): #error b
                      errorflag=True
                      print(str(linenumber)+' Use of undefined variables')
                      break

              if (inst[i][2] in label): # error f
                      errorflag=True
                      print('Misuse of labels as variables')
                      break
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break

              if (typeofinst != 'D'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break

              bincode.append(store(inst[i],flag,rega))
          if inst[i][0] == 'mul':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break

              if (typeofinst != 'A'):
                errorflag=true
                print(str(linenumber)+' Wrong syntax used for instructions')
                break

              bincode.append(mult(inst[i],flag,rega))
          if inst[i][0] == 'div':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'C'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(divn(inst[i],flag,rega))
          if inst[i][0] == 'rs':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'B'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(right(inst[i],flag,rega))
          if inst[i][0] == 'ls':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'B'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(left(inst[i],flag,rega))
          if inst[i][0] == 'xor':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break

              if (typeofinst != 'A'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              
              bincode.append(exor(inst[i],flag,rega))
          if inst[i][0] == 'or':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'A'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(Or(inst[i],flag,rega))
          if inst[i][0] == 'and':
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'A'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(And(inst[i],flag,rega))
          if inst[i][0] == 'not': # To be checked
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'C'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(inv(inst[i],flag,rega))
          if inst[i][0] == 'cmp': # To be checked
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'C'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(comp(inst[i],flag,rega))
          if inst[i][0] == 'jmp': # To be checked
              # print(typeofinst)
              # print('in jump')
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'E'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(jump(inst[i],flag,label))      
          if inst[i][0] == 'jlt': # To be checked
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break
              if (typeofinst != 'E'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(jumpiflt(inst[i],flag,rega,label))  
          if inst[i][0] == 'jgt': # To be checked
              if (haltpresent==True):
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break

              if (typeofinst != 'E'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break
              bincode.append(jumpifgrt(inst[i],flag,rega,label))      
          if inst[i][0] == 'je': # To be checked
              if (haltpresent==True): ####error i
                errorflag=True
                print(str(linenumber)+' hlt not being used as the last instruction')
                break

              if (typeofinst != 'E'):
                errorflag=True
                print(str(linenumber)+' Wrong syntax used for instructions')
                break

              bincode.append(jumpifeq(inst[i],flag,rega,label)) 

          if inst[i][0] == 'hlt':
               
               if (haltpresent==True): ####error i
                  errorflag=True
                  print(str(linenumber)+' hlt not being used as the last instruction')
                  break

               

               if (typeofinst != 'F'):
                  errorflag=True
                  print(str(linenumber)+' Wrong syntax used for instructions')
                  break

               haltpresent=True
               check,s = halt(inst[i]) 
               bincode.append(s)

if (haltpresent==False and errorflag==False): # error h
    errorflag=True
    print("Missing hlt instruction") 
#print(rega)
#print(bincode)
#print(flag)
if (errorflag==False):
  for i in bincode:
      print(i)
#print(label)
# print(var)
#print(len(bincode))
