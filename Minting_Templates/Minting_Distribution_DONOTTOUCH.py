import os
import sys
from shutil import copyfile

# Save all KEYs in arrays
with open('A_KEYS.txt', 'r') as file:
    filedata = file.read()
    KEYList = filedata.split("\n")
with open('B_PROXIES.txt', 'r') as filee:
    filedataa = filee.read()
    PROXYList = filedataa.split("\n")
    print(PROXYList)
with open('C_Directory.txt', 'r') as fileee:
    filedataaa = fileee.read()
    DIRECTORYY = filedataaa

# If less proxies are given than the amount of private keys, blank proxies are set.
diff = len(KEYList) - len(PROXYList)
if diff > 0:
    for i in range(diff):
        PROXYList.append('')

with open('D_FullConfigPaste.txt') as fileeee:
    filedataaaa = fileeee.read()
    CONFIGThing = filedataaaa

# Update Values into fresh copies of the template
for i in range(1, len(KEYList)+1):
    copyfile(DIRECTORYY + '/NFTY/Minting_Templates/Minting_Template_DONOTTOUCH.toml', DIRECTORYY + '/NFTY/Minting_Templates/Minting_Wallet_' + str(i) + '.toml')
    with open('Minting_Wallet_' + str(i) + '.toml', 'r') as file:
        filedata = file.read()
    filedata = filedata.replace("YOURPRIVATEKEYHERE", KEYList[i-1])
    filedata = filedata.replace("YOURPROXYADDRESSES", PROXYList[i-1])
    filedata = filedata.replace("FULLCONFIGPASTE", CONFIGThing)
	
    with open('Minting_Wallet_' + str(i) + '.toml', 'w') as file:
        file.write(filedata)


