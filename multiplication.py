print ('This is a multiplication table calculator')
print ('To get started, which whole number greater than 0 would you like to view? You may enter 0 to exit')
#ask user to identify sourceNumber(Source number; min value of 1 or 0 to exit)
while True:
    try:
        sourceNumber=int(input('Please enter a whole number from 1 to 10. You may enter 0 to exit.\n'))
        if (sourceNumber == 0):
            print (f'You entered {sourceNumber}. Program will now close.')
            exit()
        if ((sourceNumber>10) or (sourceNumber<1)):
            raise ValueError ('Number must be between 1 and 10')
        else:
            #ask user to identify minRangeValue(any whole number)
            while True:    
                try:
                    minRangeValue=int(input('Please enter any whole number to set minimum calculated range.\n'))
                    #ask user to identify maxRangeValue(max value of >=min and =/= > 10 + minRangeValue)
                    while True:
                        try:
                            maxCap = minRangeValue+9
                            maxRangeValue=int(input(f'To set maximum range value, please enter a whole number greater than or equal to {minRangeValue} but not greater than {maxCap}.\n'))
                            if ((maxRangeValue >= minRangeValue)and(maxRangeValue <= maxCap)):
                                #Display of multiplication handled below 
                                for i in range (minRangeValue,maxRangeValue+1):
                                    print(sourceNumber, 'x', i, '=', sourceNumber*i)
                                    continue
                            else:
                                raise ValueError (f'Value must be greater than or equal to {minRangeValue} but not greater than {maxCap}')
                            break
                        #Error handling closings
                        except ValueError:
                                print ('Incorrect input received.')
                        continue
                    break
                except ValueError:
                    print ('Incorrect input received.')
                continue
    except ValueError:
        print ('Incorrect input received.')
        continue