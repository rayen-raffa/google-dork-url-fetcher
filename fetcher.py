from decouple import config

# Credentials setup
API_KEY = config('API_KEY')
CSE_ID = config('CSE_ID')

# Change line below
DORK = 'inurl:index.php?id=2 site:fr'


print(API_KEY)
print(CSE_ID)