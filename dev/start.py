'''
start.py

This is the file in which I began testing and development
with the python requests library and API key

author: awenstrup
'''

#----------------Import statements---------------------
import requests

#----------------Global Variable Definitions-----------
#API Key Path
api_key_file_path = '../api_key.txt'

url_root = 'https://app.joinhandshake.com/api/v1'
jobs_ext = '/jobs'
users_ext = '/users'
ext = users_ext #INPUT LINE

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
#----------------Main----------------------------------
'''
Here is an example of a generic get request

requests.get(url, headers=headers, data=data)
'''
#Setup HTTP Request
init_headers()
search_student_param('Wenstrup') #INPUT LINE
print(headers)
print(params)
print(url_root + ext)

#Send HTTP Request
r = requests.get(url_root + ext, headers=headers, params=params) #INPUT LINE

#Process returned data
data = r.json()
print(data['users'][0]['first_name'])
