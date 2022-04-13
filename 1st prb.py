import time
i=0                                                           #variable for counting loop
initiator=['VAR','LET']  
state=True                                                    #variable for if...else statement
while_loop=False                                              #variable for while staetment
inp=open('testrun.txt','r') 
for line in inp: 
    i+=1
    if('//' in line):                                         #removing comments in scream file
        pos=line.find('//')
        comline=line[pos:]
        line=line.replace(comline,'')
    if('\'') in line:                                         # temporarily excluding string and including it later
        pos=line.find('\'')
        strline=line[pos:]
        line=line.replace(strline,'')
    else:
        strline=None
    
    try:
        if(any(True if ord(i) in range(97,123) else False for i in line)):    #  raising error if lowercase letter in synatx
            raise Exception 
    except Exception :
        
        print('CAPS_ERROR')
        print('line '+str(i))
        exit()

    if strline != None:
        line=line[:pos]+strline

    splitted=line.split()
    if splitted[0] in initiator and (state==True ) and while_loop==False:       # declaring variable expression
        splitted=line.split()
        
        if '=' and '(' in line:                                                 # declaring variable expression for function call
            exec(splitted[1]+'='+splitted[3]+splitted[4]+splitted[5][:-1])      #using exec() function for manipulation of string

        
        elif 'ARRAY' in line :                                                   # declaring variable expression for array

            exec(splitted[1]+'='+'[None]*'+splitted[2][-2])
        
        elif '\'' in line:                                                      # declaring variable expression for string
            ipos=line.find('\'')
            fpos=line.find('\'',ipos+1)


            exec(splitted[1]+'='+'\''+line[ipos+1:fpos]+'\'')                  #using exec() function for manipulation of string
        
        elif '=' in line:
            exec(splitted[1]+'='+splitted[3])

        else:
            try:
                if len(splitted)>3:
                    raise Exception


            except Exception:
                print('Please remove whitespace around arithmatic operators' )
                exit()
            exec(splitted[1]+'='+splitted[2][0:-1])
    
    elif splitted[0] =='PRINT' and (state==True) and while_loop==False:           #printing expression

        if '\'' in line:                                                          #printing expression for string
            b=' '.join(splitted[1:])[:-1]
            exec('print('+b+')')

        else:
            b=splitted[1][:-1]
            exec('print('+b+')')
    elif splitted[0]=='IF':                                         #if statement execution
        exec('state='+splitted[1])
        secstate=state                                              #storing boolean value in variable
    elif splitted[0]=='END' and while_loop==False:                    
        state=True
    elif splitted[0]=='ELSE':                   
        state=not(secstate)
    elif splitted[0]=='WHILE':                                       #while loop execution
                                          #variable for containing while loop commands
        while_loop=True                                              #variable to show execution is in while loop
        wtext= 'while '+splitted[1]+':'
    elif while_loop==True:
        
        
        if splitted[0] in initiator:
            wtext+='\n'+'    '+splitted[1]+'='+splitted[2]
        if splitted[0]=='PRINT':
            wtext+='\n'+'    '+'print('+splitted[1]+')'

        
    elif splitted[0] =='END' and while_loop==True:
        
        
        # xy=while_line.split()
        # exec('while'+wtext[0]+':\n'+'    '+xy[2]+'='+xy[3][:-1]+'\n'+'    '+xy[5]+'='+xy[6]+'\n')
        exec(wtext)
        while_loop=False
        while_line=None
    elif splitted[0]=='FUNC':                                                     #function declaration
        funcline='def '+splitted[1][:-1]+'('+splitted[2]+splitted[3]+':\n'        #variable containg function declaration primary line
    elif splitted[0]=='RETURN':                                                   #return statement
        funcline+='    '+'return'+splitted[1][:-1]
        exec(funcline)                                                            #using exec() function for manipulation of string
    elif splitted[0]=='HALT':                                                     #HALT command stops program execution
        time.sleep(10)
        exit()



    
    





        



        


    

