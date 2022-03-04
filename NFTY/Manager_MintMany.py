import os
import sys
from shutil import copyfile
import math

with open('./Minting_Templates/C_Directory.txt', 'r') as filee:
    filedataa = filee.read()
    DIRECTORYY = filedataa

# Meme 
# print("Are you KFish and do you use powershell? y/n")
# answer = input()
# print("Sorry we are using cmd here... :( ")


# INPUT SAFETY NOT SET


# Input collecting

print("Wallets to use(ex: 1234, 2243): ")
INPUTWallets = input()
print("")
priceTargets = []

for i in INPUTWallets:
    print("Prio for Wallet " + i + ":")
    priceTargets.append(float(input()))
    print("")

# Calculate GASGAS from Gas Limit and Tokencount on Price demand.
#GASGAS = math.ceil((priceTargets - INPUTTotalCost)*1000000000/INPUTgasLimit)
GASGAS = []
for i in priceTargets:
    GASGAS.append(i)


# Reset configFiles to templates
print("-Initializing templates")
configFiles = ["Minting_Wallet_" + i + ".toml" for i in INPUTWallets]
print("-Copying templates soon to become configs")
for i in range(len(configFiles)):
    copyfile(DIRECTORYY + '/NFTY/Minting_Templates/' + configFiles[i], DIRECTORYY + '/NFTY/TempDump/' + configFiles[i])

# Overwrite values to input
print("-Changing values in configs " + INPUTWallets)
for i in range(len(configFiles)):
    with open("./TempDump/" + configFiles[i], 'r') as file:
        filedata = file.read()
    filedata = filedata.replace("GASGAS", str(GASGAS[i]))
    with open("./TempDump/" + configFiles[i], 'w') as file:
        file.write(filedata)

print("You are paying for Wallets:")
print(INPUTWallets)
print("At prices:")
print(GASGAS)

# Confirmation message
print("")
print("Please Confirm.")
print("y / n")

# Run bots on cmd   'start cmd.exe /k "nfty.exe -c ' +  './TempDump/' + configFiles[i] + '"'
confirmation = input()
if (confirmation=='y'):
    print("Running bots")
    res = 'start cmd.exe /k "nfty.exe'
    for i in range(len(configFiles)):
        res += ' -c ./TempDump/' + configFiles[i]
    res +=  '"'
    
    print("COMMAND: "+res)
    os.system(res)
else: 
    print("Terminating")