import twint
import re


#Valid Bitcoin address examples
phrase1 = "My bitcoin address is :1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 yo"
phrase2 = "My bitcoin address is :1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 and 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy yo"
phrase3 = "  3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy"
phrase4 = "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq"

#Non-Valid Bitcoin address examples
phrase5 = "2BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"
phrase6 = "5J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy"
phrase7 = "b1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq"

#Bitcoin actual (02/2020) regexpr
regexpr = '(bc1|[13][a-zA-HJ-NP-Z0-9]{25,39})'


#Function list with addresses in Bitcoin form
def match(regexpr,phrase):
    return re.findall(regexpr,phrase)

#Function return True if one address is in Bitcoin form
def matchbool(regexpr,phrase):
    if (re.findall(regexpr,phrase) != []):
        return True
    return False
    
#Tests
print(match(regexpr,phrase1))
print(matchbool(regexpr,phrase1))
print(match(regexpr,phrase2))
print(matchbool(regexpr,phrase2))
print(match(regexpr,phrase5))
print(matchbool(regexpr,phrase5))

#Configure Twint

c = twint.Config()
c.Search = "Bitcoin address"
c.Store_json = True


# Run
#twint.run.Search(c)
