import time
import os
from random import *
start=1
if start==1:
	print("[÷] WELCOME TO USERNAME GENERATOR V1.0 BY CATHWULF\n")
	luser=int(input("[1] Username Length? : "))
	while (luser<3 or luser>15):
		print("! Most be between 4-15 !")
		luser=int(input("Username Length? : "))
	muser=int(input("[2] How many username? : "))
	while (muser>1001):
		print("! Most be less than 1000 !")
		muser=int(input("How many username? : "))
	print("\n")
	usr=""
	total=0
	for i in range(muser):
		for i in range(luser):
			c=chr(randint(97,122))
			usr=usr+c
			if int(len(usr))==luser:
				break
		#print(usr)
		total=total+1
		f = open("usernames.txt", "a")
		f.write(usr+"\n")
		f.close()
		usr=""
		os.system("clear")
		print("---------------------------->Generating<--------------------------------")
		print("------------------------------->",total,"<------------------------------------")
		time.sleep(0.2)
	print("\nDone. you generated :",total,"usernames")
	print("Your usernames saved as 'usernames.txt'")
	input("\nPress Ok to exit")