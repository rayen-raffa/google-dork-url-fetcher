import urllib
import requests
import os
from decouple import config

# Credentials setup
API_KEY = config('API_KEY')
CSE_ID = config('CSE_ID')
API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"

# Change lines below as needed
DORK = 'inurl:index.php?id= site:com'
OUT_FILE = "./urls.csv"
if not os.path.isfile(OUT_FILE):
    print("Output file missing ! Creating {}".format(OUT_FILE))
    with open(OUT_FILE,'w') as f:
        f.write('dork,url')

# Given DORK
print("Fetching urls for dork : {}".format(DORK))
# encode to url
ENCODED_DORK = urllib.quote_plus(DORK)
url_count = 0
# for each resp page
for page in range(10):
    start = page * 10 + 1

    # get json data from api
    API_ENDPOINT = "https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&q={2}&start={3}".format(API_KEY,CSE_ID,ENCODED_DORK,start)
    print("fetching page {}".format(page+1))

    try:
        resp = requests.get(API_ENDPOINT)
    except Exception as e:
        print("ERROR fetching from page {} ! Skipping ...".format(page+1))
    
    if(resp):
        json_data = resp.json()
        try:
            items = json_data["items"]
            print("Writing page {} to urls.csv ..".format(page+1))
        except KeyError:
            print("ALERT : No response found in page {} ! Skipping ...".format(page+1))
            items = []
        
        with open("./urls.csv", 'a') as res_file:
            # for each url
            for item in items: 
                # append to res file
                res_file.write("\n{},{}".format(DORK,item["link"]))
                url_count = url_count + 1

print("FOUND {} urls in total !".format(url_count))




# print(API_ENDPOINT)
# print(API_KEY)
# print(CSE_ID)
# print(resp.json())
