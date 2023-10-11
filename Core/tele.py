import requests
from datetime import datetime

API_TOKEN='6568779492:AAG70Q0c3KmkzaCG19xNAG9Bi5iLh-CdDGo'
CHATID='871843486'

def sendmsg(message):
        apiURL = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={CHATID}&text={message}'
        requests.post(apiURL)
    
