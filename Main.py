import twint
import re
import json
import argparse
import os
import sys
import datetime
import inspect
import time

# Python program to show time by perf_counter()  
from time import perf_counter 



# Bitcoin actual adress regexpr (05/2020)
regexpr = '(?:(?!#)\W((?:[12359cKLmn]|bc1|xpub|xprv|tpub|tprv|tb1)[a-km-zA-HJ-NP-Z1-9]{25,})\W)'


# Function returns list with addresses in Bitcoin form
def match(regexpr,phrase) :
    return re.findall(regexpr,phrase)

# Function return True if one address is in Bitcoin form
def matchbool(regexpr,phrase) :
    if (re.findall(regexpr,phrase) != []) :
        return True
    return False

#Function checking output of Twint and write 
def checkOutput(output,type) :
	toAdd = []
	addressesRemember = []
	nbre = 0
	stamp = ""
	for i in output :
		stamp = i.datestamp +" "+ i.timestamp
		#print(output)
		addresses = match(regexpr,i.tweet)
		localAdr = []
		for adr in addresses:
			if(not(adr in localAdr)):
				localAdr.append(adr)
		if (match(regexpr,i.tweet)!=[] and not(localAdr in addressesRemember)) :
			
			nbre+=len(localAdr)
			jsonObj = {'username' : i.username,'user ID' : i.user_id,'addresses' : localAdr, 'tweet' : i.tweet}
			toAdd.append(jsonObj)
			addressesRemember.append(localAdr)
	if (type == 'adresse') :
		with open('addresses.json', 'w') as outfile:
			json.dump(toAdd,outfile,indent=2)
	if (type == 'followers') :
		with open('followers.json', 'w') as outfile:
			json.dump(toAdd,outfile,indent=2)
	print('---------------------------------------------------------------------------------')
	print('Nombre de tweets : '+str(len(output))+' | Nombre d\'adresses : ' +str(nbre) )
	pourcent=0
	if (len(output)>0):
		pourcent = (nbre/len(output))*100
	print('Soit : '+str(round(pourcent,2))+'%')
	print('---------------------------------------------------------------------------------')

	return stamp


# Main function
def main():
	#Arguments
	parser = argparse.ArgumentParser(description='Search Bitcoin addresses on Twitter')
	parser.add_argument('-p',nargs='?',help="Search phrase. 'bitcoin address' by default")
	parser.add_argument('-ts',nargs='?',help="Tweets since date (Format : YYYY-MM-DD). 2016-01-01 by default")
	parser.add_argument('-tu',nargs='?',help="Tweets until date (Format : YYYY-MM-DD). 2016-12-31 by default")
	args = parser.parse_args()
	# Twint basic configuration
	cs = twint.Config()
	cs.Search = "bitcoin address"
	cs.Store_object = True
	cs.Custom['tweet']=['tweet']
	cs.Store_object_tweets_list
	cs.Limit = 800
	#Hide output in terminal
	cs.Hide_output = True

	#Default search : period from 2016 to 2017
	stopDate = datetime.datetime(2016, 1, 1)

	untilDate = datetime.datetime(2016, 12, 31, 23, 59, 59)
        
	#Automatically convert uppercase in lowercase
	cs.Lowercase = True

	#Arguments passed by user
	if args.p :
		#Search phrase
		cs.Search = args.p

	if args.tu :
		#Split until date
		untilSplitted = args.tu.split("-", 3)
		untilDate = datetime.datetime(int(untilSplitted[0]), int(untilSplitted[1]), int(untilSplitted[2]), 23, 59, 59)
		

	if args.ts :
		#Split since date
		stopSplitted = args.ts.split("-", 3)

		newStopDate = datetime.datetime(int(stopSplitted[0]), int(stopSplitted[1]), int(stopSplitted[2]))

		#Check since date before until date
		if newStopDate < untilDate :
			stopDate = newStopDate
			
		else :
			print("Votre date : ",newStopDate," est > a la date de fin : ",untilDate,". \nVeuillez recommencer en entrant une date anterieure a la date de fin.")
			return

	# Start the stopwatch / counter 
	t1_start = perf_counter()

	while(stopDate < untilDate):
		cs.Until = str(untilDate)

		# Collect tweets
		twint.run.Search(cs)

		# Create list to parse
		tweets = twint.output.tweets_list
		# Checking + parsing the tweets and write them in Json file
		untilDate = datetime.datetime.strptime(checkOutput(tweets,'adresse'), "%Y-%m-%d %H:%M:%S")

		print(str(untilDate))
		time.sleep(30)

	# Twint followers configuration
	#f = twint.Config()
	#f.Search = "bitcoin address"
	#f.Custom['tweet']=['tweet']
	#f.Store_object = True
	#f.Store_object_tweets_list
	#f.Limit = 100

	#twint.run.Followers(f)
	#followers = twint.output.follows_list
	#print(followers)
	#checkOutput(followers,'followers')

	t1_stop = perf_counter()

	print("Durée de la recherche :",round(((t1_stop-t1_start)/60),2),'min')
	print('---------------------------------------------------------------------------------')
main()
