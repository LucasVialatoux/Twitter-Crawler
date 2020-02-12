import twint
import re
import json
import argparse


# Bitcoin actual adress regexpr (02/2020)
# Adresses beginning with bc1 or 1 or 3 and finishing with space or EOL
regexpr = '([13|(bc1)][a-zA-HJ-NP-Z0-9]{25,39})'


# Function returns list with addresses in Bitcoin form
def match(regexpr,phrase) :
    return re.findall(regexpr,phrase)

# Function return True if one address is in Bitcoin form
def matchbool(regexpr,phrase) :
    if (re.findall(regexpr,phrase) != []) :
        return True
    return False

#Function checking output of Twint and write 
def checkOutput(output) :
	toAdd = []
	for i in output :
		print(output)
		if (match(regexpr,i.tweet)!=[]) :
			# Address with \n at the end
			addresses = match(regexpr,i.tweet)
			jsonObj = {'username' : i.username, 'addresses' : addresses, 'tweet' : i.tweet}
			toAdd.append(jsonObj)
	with open('addresses.json', 'w') as outfile:
		json.dump(toAdd,outfile,indent=2)

# Main function
def main():
	#Arguments
	parser = argparse.ArgumentParser(description='Search Bitcoin address in Twitter')
	parser.add_argument('-n', type=int, nargs='?',help='Number of threads. 100 by default')
	parser.add_argument('-s',nargs='?',help="Search phrase. 'my bitcoin address' by default")
	parser.add_argument('-u',nargs='?',help="Username to look after. No username by default")
	parser.add_argument('-t',nargs='?',help="Tweets since date (Format : YYYY-MM-DD). Last tweets by default")
	parser.add_argument('-y',nargs='?',help="Tweets before specified year. Last tweets by default")
	args = parser.parse_args()
	# Twint basic configuration
	c = twint.Config()
	c.Search = "my bitcoin address"
	c.Limit = 100
	c.Store_object = True
	c.Custom['tweet']=['tweet']
	c.Store_object_tweets_list

	#Arguments passed by user
	if args.n :
		c.Limit = args.n
	if args.s :
		c.Search = args.s
	if args.u :
		c.Username = args.u
	if args.t :
		c.Since = args.t
	if args.y :
		c.Year = args.y

	# Collect tweets
	twint.run.Search(c)

	# Create list to parse
	tweets = twint.output.tweets_list

	# Checking + parsing the tweets and write them in Json file
	checkOutput(tweets)

main()
