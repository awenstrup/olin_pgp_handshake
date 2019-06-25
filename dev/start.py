'''
start.py

This is the file in which I began testing and development
with the python requests library and API key

author: awenstrup
'''

#----------------Import statements---------------------
import requests

#----------------Global Variable Definitions-----------
api_key_file_path = '../api_key.txt'
api_key = ''

#----------------Function definitions------------------
def get_api_key(path):
    file = open(path, 'r')
    key = file.read().strip()
    return key

#----------------Main----------------------------------
api_key = get_api_key(api_key_file_path)
print(api_key)
