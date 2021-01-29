import numpy as np
import helpers
import Config

def main():
    print('''

    ========================================== ''')
    print ("bDebug = " + str(Config.bDebug))

    ## Initial debug code
    if Config.bDebug:
        strSiren="123456789"
        strSiren="120027016"
        ## 100000017 (présidence de la république), 150000966 (école navale)
        strExample = ("123456789","120027016","100000017", "150000966")
        for strSiren in strExample:
            strRet1 = "OK" if helpers.IsLuhnValid(strSiren)  else  "invalide"     
            strRet2 = "OK" if helpers.luhn(strSiren) else  "invalide"     
            print('nSiren :'+ strSiren + ' IsLuhnValid: [' + strRet1 + '],  luhn: [' +strRet2 +'].')

    ## For préfixe "150", add values and keep the ones that are OK:
    strPrefix ="150"
    nLast = 1000
    nScope = range (1,nLast)
    strSirensOK = []
    strSiretsOK = []
    strTVAOK = []
    for i in nScope:
        strSiren =strPrefix + str(i).zfill(6)
        bSirenValid1 = helpers.IsLuhnValid(strSiren) 
        bSirenValid2 = helpers.luhn(strSiren) 
        strRet1 = "OK" if bSirenValid1  else  "invalide"     
        strRet2 = "OK" if bSirenValid2 else  "invalide"     
        if bSirenValid1: 
            strSiret = helpers.CreateSiretfromSiren(strSiren,"0001")
            ## Double check
            bSiretValid = helpers.IsLuhnValid(strSiret) 

            ## strTva = CreateTvafromSirer(strSiret,"0001")
            # Clé TVA = [12 + 3 × (SIREN modulo 97)] modulo 97
            nCleTVA = (12 + (3 * (int(strSiren) % 97))) % 97
            strTVA = "FR" + str(nCleTVA).zfill(2) + strSiren
            ##
            if Config.bDebug:
                print('nSiren :'+ strSiren + ' IsLuhnValid: [' + strRet1 + '] Siret :'+ strSiret + ' IsLuhnValid: [' + str(bSiretValid) + "], strTVA:" + strTVA + '].')
            ## copy to Text
            print(strSiren + chr(9) + strSiret + chr(9) + strTVA)

            strSirensOK.append(strSiren)
            strSiretsOK.append(strSiret)
            strTVAOK.append(strTVA)
            ## ---
    ## ---          
    nLen = len(strSirensOK)
    print ("strSirensOK.count :" + str(nLen) + ", sur " + str(nLast) + " testés")
    return nRet

    ## strTrioStart = "999"
    ## nStart=
    ## num = range(startline, endline)
    ## for 

nRet = main()

