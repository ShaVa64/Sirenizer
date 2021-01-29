import numpy as np
import Config


def CreateSiretfromSiren(strSiren,strNic4):
    ## calc LUHN for these 13 digits
    ## Add the right 14th digit
    sSiret13 = strSiren + strNic4
    nAdditionalRightMostDigit = AddDigitToMakeLuhnValid(sSiret13)                     
    return sSiret13+ str(nAdditionalRightMostDigit)


def AddDigitToMakeLuhnValid(strValue):                     
    ## Add '0' at last position so that the added value doesn't change positions
    nLuhnVal = CalcLuhnSum(strValue + "0")
    nLuhnValMod = nLuhnVal % 10
    nAdditionalRightMostDigit = 0 if nLuhnValMod==0 else 10 - nLuhnValMod
    return nAdditionalRightMostDigit


def CalcLuhnSum(strValue):                     
    nLuhnVal=0
    nPos=0
    # from right to left
    for c in reversed(strValue):
        nThisRawVal = int(c)
        nPrefixBase = (nPos % 2)
        nPrefix = (nPrefixBase+1)
        nThisLuhnVal = nPrefix * nThisRawVal
        if nThisLuhnVal >=10:
            nThisLuhnVal = 1+nThisLuhnVal-10
            ## ....
            if Config.bDebug:            
                print ("c:[" + c + "], nThisLuhnVal:["+ str(nThisLuhnVal) + "], nPos:[" + str(nPos) + "], nPrefixBase:["+ str(nPrefixBase) + "], nPrefix:[" + str(nPrefix) +"].")
            ## ....
        nLuhnVal += nThisLuhnVal
        nPos += 1
    return nLuhnVal



def IsLuhnValid(strValue):                     
    nLuhnVal = CalcLuhnSum(strValue)
    if (nLuhnVal % 10) == 0:
        return True
    else:
        return False


def luhn(ccn):
    c = [int(x) for x in ccn[::-2]] 
    u2 = [(2*int(y))//10+(2*int(y))%10 for y in ccn[-2::-2]]
    return sum(c+u2)%10 == 0

