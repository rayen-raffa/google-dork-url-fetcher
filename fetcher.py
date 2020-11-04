import urllib
import requests
from decouple import config

# Credentials setup
API_KEY = config('API_KEY')
CSE_ID = config('CSE_ID')
API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
# Change line below
DORK = 'inurl:index.php?id= site:fr'


# Given DORK
# encode to url
ENCODED_DORK = urllib.quote_plus(DORK)
# for each resp page
for page in range(10):
    start = page * 10 + 1
    payload = {
        'cx': CSE_ID,
        'key': API_KEY,
        'q': ENCODED_DORK,
        'start': start
    }
    # get json data from api
    print("fetching page {}".format(page+1))
    
    try:
        resp = requests.get(API_ENDPOINT, params=payload)
    except Exception as e:
        print("ERROR fetching from page {} ! Skipping ...".format(page+1))
    
    
#   for each url
#       append te res file

# API_ENDPOINT = "https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&q={2}".format(API_KEY,CSE_ID,ENCODED_DORK)


print(API_ENDPOINT)
print(API_KEY)
print(CSE_ID)
print(resp.json())
