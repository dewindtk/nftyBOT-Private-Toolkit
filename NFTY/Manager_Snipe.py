import os
import sys
from shutil import copyfile

with open('./Sniping_Templates/C_Directory.txt', 'r') as filee:
    filedataa = filee.read()
    DIRECTORYY = filedataa

# Meme 
# print("Are you KFish and do you use powershell? y/n")
# answer = input()
# print("Sorry we are using cmd here... :( ")


# INPUT SAFETY NOT SET


# Input collecting
print("-In order, hit enter after every input: Wallets, slug, priceTarget, maxprio, maxgas.")
print("")
print("Wallets(ex: 12345, 1142): ")
INPUTwallets = input()
print("")
print("Slug(ex: ether-orcs): ")
INPUTslug = input()
print("")
print("TargetPrice(ex: 0.35, 1): ")
INPUTtarget = input()
print("")
print("maxPrio(ex: 20): ")
INPUTmaxprio = input()
print("")
print("maxGas(ex: 300): ")
INPUTmaxgas = input()
print("")

# reset configFiles to templates
print("-Initializing templates")
configFiles = ["Sniping_Wallet_" + i + ".toml" for i in INPUTwallets]
print("-Copying templates soon to become configs")
for i in range(len(configFiles)):
    copyfile(DIRECTORYY + '/NFTY/Sniping_Templates/' + configFiles[i], DIRECTORYY + '/NFTY/TempDump/' + configFiles[i])

# Overwrite values to input
print("-Changing values in configs " + INPUTwallets)
for i in range(len(configFiles)):
    with open("./TempDump/" + configFiles[i], 'r') as file:
        filedata = file.read()
    filedata = filedata.replace("INPUTSLUG", INPUTslug)
    filedata = filedata.replace("INPUTTARGET", INPUTtarget)
    filedata = filedata.replace("INPUTMAXGAS", INPUTmaxgas)
    filedata = filedata.replace("INPUTMAXPRIO", INPUTmaxprio)
    with open("./TempDump/" + configFiles[i], 'w') as file:
        file.write(filedata)

# Confirmation message
print("")
print("Please Confirm.")
print("y / n")

# Run bots on cmd
confirmation = input()
if (confirmation=='y'):
    print("Running bots")
    for i in range(len(configFiles)):
        os.system('start cmd.exe /k "nfty.exe -c ' +  './TempDump/' + configFiles[i] + '"')
else: 
    print("Terminating")
