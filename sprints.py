def MyFunc(*list):
    sumEvenInt = 0
    countEventInt = 0
    maxFloat = -10e6
    intFound = False
    floatFound = False
    
    for i in list:
        if(type(i) == int):
            intFound = True
            if(i%2 == 0):
                sumEvenInt += i
                countEventInt += 1
                
        elif(type(i) == float):
            if(not floatFound):
                floatFound = True
                maxFloat = i
            else:
               if( i > maxFloat):
                   maxFloat = i
                    
    if(intFound or floatFound):
        return sumEvenInt/countEventInt, maxFloat
      
    if(maxFloat == -10e6):
        if(countEventInt == 0 && intFound) 
            return str("No even integers"), str("No floats")
        return str("No even integers"), maxFloat
      
    if(maxFloat == -10e6):
      return sumEvenInt/countEventInt,str("No floats")
    
    return 0,0
