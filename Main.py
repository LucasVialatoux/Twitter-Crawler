import twint
import re
import json
import argparse
import os
import sys

# Python program to show time by perf_counter()  
from time import perf_counter 



# Bitcoin actual adress regexpr (02/2020)
regexpr = '((?:[12359cKLmn]|bc1|xpub|xprv|tpub|tprv|tb1)[a-zA-HJ-NP-Z0-9]{25,})'


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
	nbre = 0
	for i in output :
		#print(output)
		if (match(regexpr,i.tweet)!=[]) :
			addresses = match(regexpr,i.tweet)
			nbre+=len(addresses)
			jsonObj = {'username' : i.username,'user ID' : i.user_id, 'addresses' : addresses, 'tweet' : i.tweet}
			toAdd.append(jsonObj)
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


# Main function
def main():
	#Arguments
	parser = argparse.ArgumentParser(description='Search Bitcoin addresses on Twitter')
	parser.add_argument('-n', type=int, nargs='?',help='Number of threads. 100 by default')
	parser.add_argument('-p',nargs='?',help="Search phrase. 'my bitcoin address' by default")
	parser.add_argument('-u',nargs='?',help="Username to look after. No username by default")
	parser.add_argument('-ts',nargs='?',help="Tweets since date (Format : YYYY-MM-DD). Last tweets by default")
	parser.add_argument('-tu',nargs='?',help="Tweets until date (Format : YYYY-MM-DD). Last tweets by default")
	parser.add_argument('-y',nargs='?',help="Tweets before specified year. Last tweets by default")
	args = parser.parse_args()
	# Twint basic configuration
	c = twint.Config()
	c.Search = "bitcoin address"
	c.Store_object = True
	c.Custom['tweet']=['tweet']
	c.Store_object_tweets_list
	c.Limit = 100
	#Hide output in terminal
	c.Hide_output = True

	#Automatically convert uppercase in lowercase
	c.Lowercase = True

	#Arguments passed by user
	if args.n :
		c.Limit = args.n
	if args.p :
		c.Search = args.p
	if args.u :
		c.Username = args.u
	if args.ts :
		c.Since = args.ts
	if args.tu :
		c.Until = args.tu
	if args.y :
		c.Year = args.y

	# Start the stopwatch / counter 
	t1_start = perf_counter()

	# Collect tweets
	twint.run.Search(c)

	# Create list to parse
	tweets = twint.output.tweets_list
	# Checking + parsing the tweets and write them in Json file
	checkOutput(tweets,'adresse')

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
