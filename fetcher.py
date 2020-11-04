from decouple import config

# Credentials setup
API_KEY = config('API_KEY')
CSE_ID = config('CSE_ID')

# Change line below
DORK = 'inurl:index.php?id=2 site:fr'



# Given DORK
# encode to url
# get json data from api
# for each resp page
#   for each url
#       append te res file

API_ENDPOINT = "https://www.googleapis.com/customsearch/v1?key={0}&cx={1}&q={2}".format(API_KEY,CSE_ID,ENCODED_DORK)
print(API_KEY)
print(CSE_ID)