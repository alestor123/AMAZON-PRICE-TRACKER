# import required files and modules
import requests
from bs4 import BeautifulSoup
import time
# set the headers and user string
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
# send a request to fetch HTML of the page
response = requests.get('https://www.amazon.in/Lenovo-L22e-20-Monitor-Display-inputs/dp/B07SGDWMCG/ref=sr_1_1?dchild=1&keywords=monitor+lenovo&qid=1595088224&s=electronics&sr=1-1', headers=headers)
