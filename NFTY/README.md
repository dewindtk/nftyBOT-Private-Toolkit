This Toolkit only works on Windows. It uses nfty.exe, nftyBOT. I cannot guarantee the safety of your Private keys as the code 
of the bot itself is hidden behind an executable. Proceed on your own risk and use alt wallets.
This toolkit supports up to 9 wallets. Not more in this current build.

Please Simply download the entire folder, unzip to start using :]
PLease do not change the folder name after unzipping

-First, fill in your nfty credentials in credentials.toml. Your Token ID and private key which holds the token.
-Replace the nfty.exe with the lateset version on their disocrd.

-For Opensea Sniping:

	1 - Go to Sniping_Templates and fill in A_Keys with your private keys, one on each row.
	2 - Fill in the B_Proxies with proxies on each row corresponding to the private keys in order. 
		If you do not wish to connect any proxies either leave blank or leave a blank row.
		Syntax: http://user:pass@ip:port
	3 - Fill in C_Directory where you have stored this NFTY folder. There is a format example within already. 
	4 - Click D_Initialise_Sniping_Templates.bat which will generate Template files from the above steps. 
		You can delete these whenever you want and rerun the bat.
		Do not touch the other files.
	5 - Go back to the main folder and run START_SNIPE.bat, which will run Manager_Snipe.py. 
		The cmd will ask you for the Values which are needed.
		Try not to typo, if you do close the window and the bot will stop.
		Your inputs will then be used to fill in the gaps in the template files created on step 4 and these
		config files will be saved in the folder TempDump. These will be replaced every time you run the bat.
		You are free to delete these as well. Just do not rename the folder.
	Your bots should be running now :] it only detects new listings, not already exsisting ones.

-For Contract minting:
	
	1 - 2 - 3 - The same. We have seperate files for seperate occations to keep the operation clean.
	4 - This is where you will need to improvise. On the example config in D_FullConfigPaste.txt you can see
		that you can change the contract address you are minting from, the function name and the input arguments
		freely. You will need to estimate your GAS LIMIT yourself, or acquire a simulated result from the nfty-
		discord support ticket system. HERE IMPORTANT: you will require to have 'gas_fee' and 
		'priority_fee' set to 'GASGAS'. This will be explained in the next steps.
	5 - Run E_Initialise_Minting_Templates to generate your Templates tied to the above steps.
		Do not touch the other files.
	6 - Go back to the main folder and run START_MINT.bat, which will run Manager_Mint.
		This one will ask you for similar info but the cool part comes last: You may input a target price for which you 
		would like to mint a Token for each wallet and it will automatically calculate based on the gas limit 
		(which you must ofc give the same value as what you put in step 4) the MaxGas and the MaxPrio fees. 
		These are set to be equal so that you will pay approximately (rounded down) the amount you have targetted for 
		each wallet, as long as you have enough eth in that wallet. This is how botters cook, by setting a target price 
		which you are prepared to pay else leave the mint and move on to the next one.
	7 - Your bot should now be trying to push the mint in every block. Care, they will keep minting until you stop them,
		or your wallet runs out of eth. Never put more eth than your target price + transfer gas if you do not wish that.

-Feel free to modify the code. It's simple python whcih you can play around with if you do not like smt :]
Donations to kaikun.eth pls JHHAHHHAHA

Kai 
