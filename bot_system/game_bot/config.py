import os
from dotenv import dotenv_values 

dict_tokens = dotenv_values(".env")   

MANIFEST_URL = dict_tokens['MANIFEST_URL']