'''
start.py

This is the file in which I began testing and development
with the python requests library and API key

author: awenstrup
'''

#----------------Import statements---------------------
import requests
from user import User

#----------------Global Variable Definitions-----------
#API Key Path
api_key_file_path = '../api_key.txt'

#URL fragments
url_root = 'https://app.joinhandshake.com/api/v1'
jobs_ext = '/jobs'
users_ext = '/users'
ext = users_ext #INPUT LINE

#Request sections
headers = {}
params = {}

#----------------Function definitions------------------

#Create HTTP headers
def get_api_key(path):
    file = open(path, 'r')
    key = file.read().strip()
    return key

def add_auth_header(key):
    headers['Authorization'] = 'Token token=\"' + key + '\"'
    # {Authorization: Token token=API_KEY_HERE}

def add_content_type_header():
    headers['Content-Type'] = 'application/json'
    # {Content-Type: appication/json}

def add_cache_header():
    headers['Cache-Control'] = 'no-cache'
    # {Cache-Control: no-cache}

def init_headers():
    k = get_api_key(api_key_file_path)
    add_auth_header(k)
    add_content_type_header()
    add_cache_header()

#Set parameters
def search_student_param(string):
    params['query'] = string

def set_reponse_size(size):
    params['per_page'] = size

def load_user(response):
    '''
    Returns a User object (with username, first
    and last names, and class name), given a JSON
    object representing a user
    '''

    uid = response['username']
    email = response['email_address']
    type = response['user_type']
    first = response['first_name']
    last = response['last_name']
    class_name = response['school_year_name']
    return User(uid, email, type, first, last, class_name)

def load_users_from_year(users, year):
    '''
    Returns all the users of a certain class
    year
    '''
    out = {}
    for user in users:
        if user['user_type'] == 'Students' and user['school_year_name'] == year:
            out[user['username']] = load_user(user)

    for key in out:
        print(out[key])
    return(out)



#----------------Main----------------------------------
'''
Here is an example of a generic get request

requests.get(url, headers=headers, data=data)
'''
#Setup HTTP Request
init_headers()
#search_student_param('Senior') #INPUT LINE
set_reponse_size(4000) #INPUT LINE, includes all users
print(headers)
print(params)
print(url_root + ext)

#Send HTTP Request
#Request only users that match 'Wenstrup'
r1 = requests.get(url_root + ext, headers=headers, params={'query': 'Wenstrup'}) #INPUT LINE
#Request all users
r2 = requests.get(url_root + ext, headers=headers, params=params) #INPUT LINE

#Process returned data
data1 = r1.json()
alex = load_user(data1['users'][1])
print(alex)
print()

data2 = r2.json()
#print(data2)
users = load_users_from_year(data2['users'], 'Senior')
