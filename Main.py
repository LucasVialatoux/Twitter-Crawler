import twint
import re
import json


# Bitcoin actual adress regexpr (02/2020)
# Adresses beginning with bc1 or 1 or 3 and finishing with space or EOL
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
	# Twint basic configuration
	c = twint.Config()
	c.Search = "bitcoin address"
	c.Limit = 100
	c.Store_object = True
	c.Custom['tweet']=['tweet']
	c.Store_object_tweets_list
	# Collect tweets
	twint.run.Search(c)

	# Create list to parse
	tweets = twint.output.tweets_list

	# Checking + parsing the tweets and write them in Json file
	checkOutput(tweets)

main()
