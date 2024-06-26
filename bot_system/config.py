import os
from dotenv import dotenv_values 

if not ".env" in os.listdir():
    with open(".env", "w") as f:
        for key, value in os.environ.items():
            f.write(f"{key}='{values}'")

dict_tokens = dotenv_values(".env")   

TOKEN_BOT_GAME = dict_tokens['TOKEN_BOT_GAME']
LINK_BOT_GAME = dict_tokens['LINK_BOT_GAME']

TOKEN_BOT_EXCHANGE = dict_tokens['TOKEN_BOT_EXCHANGE']
LINK_BOT_EXCHANGE = dict_tokens['LINK_BOT_EXCHANGE']

TOKEN_BOT_CASINO = dict_tokens['TOKEN_BOT_CASINO']
LINK_BOT_CASINO = dict_tokens['LINK_BOT_CASINO']
