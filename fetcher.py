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

    # get json data from api
    API_ENDPOINT = "https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&q={2}&start={3}".format(API_KEY,CSE_ID,ENCODED_DORK,start)
    print("fetching page {} - {}".format(page+1,API_ENDPOINT))
    
    try:
        resp = requests.get(API_ENDPOINT)
    except Exception as e:
        print("ERROR fetching from page {} ! Skipping ...".format(page+1))
    
    if(resp):
        json_data = resp.json()
        try:
            items = json_data["items"]
        except KeyError:
            print("ALERT : No response found in page {} ! Skipping ...".format(page+1))
            items = []
        # for each url
        for item in items:
            print(item["link"])

#       append te res file


print(API_ENDPOINT)
print(API_KEY)
print(CSE_ID)
# print(resp.json())
